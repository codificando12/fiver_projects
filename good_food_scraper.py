"""
Title
Python - Need web scraper for dynamic site

Description
I'm looking to build a web scraper on python. Looking to collect item name, price, restaurant information 
(name, merchant id, location). Need at least 3 items were collected for each merchant and minimum 30 
merchants scraped from the site.

From https://gofood.co.id/jakarta/restaurants/near-me?page=1

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import time

def run():

    driver = webdriver.Chrome(executable_path= r'C:/chrome-driver/chromedriver.exe')
    driver.get('https://gofood.co.id/jakarta/restaurants/near-me?page=1')
    driver.maximize_window()
    times = 1
    for restaurant in range(1, 31):
        try:
            shop = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, f'//*[@id="__next"]/div/div[3]/div[1]/div[{restaurant}]/a')))
        except:
            time.sleep(30) # desde acá
            driver.refresh()
            time.sleep(5)
            for j in range(times):
                driver.execute_script("window.scrollBy(0, 1000);")
                time.sleep(3)
            shop = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, f'//*[@id="__next"]/div/div[3]/div[1]/div[{restaurant}]/a')))
            times += 1
        try:
            shop.click()
        except ElementClickInterceptedException:
            print("El clic en el elemento fue interceptado")
            driver.execute_script("window.scrollBy(0, 200);")
            shop = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, f'//*[@id="__next"]/div/div[3]/div[1]/div[{restaurant}]/a')))
            shop.click()
        items = 0
        menu_div = 1
        food_div = 1
        try:
            error = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                            (By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/span')))
            if error.text == "Belum bisa pesen di resto dan area ini. Eksplor resto lain, yuk.":
                driver.back()
                menu_div = 1
                food_div = 1
                print(restaurant)
        except:
            while items < 3:
            
                rest_name = WebDriverWait(driver,10).until(EC.presence_of_element_located(
                    (By.XPATH, ' //*[@id="__next"]/div/div[2]/div[1]/div[1]/div[1]/div[1]/h1')))
                loc_distance = WebDriverWait(driver,10).until(EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/div[2]/div/div[2]/div/p')))
                loc_city =  WebDriverWait(driver,10).until(EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/div[2]/div/div[2]/p')))
                try:
                    food_name = WebDriverWait(driver,10).until(EC.presence_of_element_located(
                        (By.XPATH, f'/html/body/div[2]/div/div[2]/div[3]/div/div[{menu_div}]/div/div[{food_div}]/div/div[1]/div[1]/h3')
                    ))
                    food_price = WebDriverWait(driver,10).until(EC.presence_of_element_located(
                        (By.XPATH, f'/html/body/div[2]/div/div[2]/div[3]/div/div[{menu_div}]/div/div[{food_div}]/div/div[1]/div[1]/div/div/span')
                    ))
                    food_div += 1
                except:
                    menu_div += 1
                    food_name = WebDriverWait(driver,10).until(EC.presence_of_element_located(
                        (By.XPATH, f'/html/body/div[2]/div/div[2]/div[3]/div/div[{menu_div}]/div/div[{food_div}]/div/div[1]/div[1]/h3')
                    ))
                    food_price = WebDriverWait(driver,10).until(EC.presence_of_element_located(
                        (By.XPATH, f'/html/body/div[2]/div/div[2]/div[3]/div/div[{menu_div}]/div/div[{food_div}]/div/div[1]/div[1]/div/div/span')
                    ))
                    food_div += 1
                print("restaurant: " + rest_name.text)
                print(f"location: {loc_city.text} {loc_distance.text}")
                print(driver.current_url)
                print(food_name.text)
                print(food_price.text)
                items += 1
                time.sleep(3)
            driver.back()
            menu_div = 1
            food_div = 1
            print(restaurant)
    driver.close()
if __name__ == "__main__":
    run()
# Kota-kota yang ada GoFood
# /html/body/div[2]/div/div[2]/div/div[2]/div/div[1]/div/h3

# /html/body/div[2]/div/div[2]/div[3]/div/div[1]/div/div[1]/div
# //*[@id="section--0"]/div/div[2]
# div = /html/body/div[2]/div/div[2]/div[3]/div/div[2]/div/div[1]
# food name: /html/body/div[2]/div/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/div[1]/h3
# food prince: /html/body/div[2]/div/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div/span

# div : /html/body/div[2]/div/div[2]/div[3]/div/div[2]/div/div[2]
# food name: /html/body/div[2]/div/div[2]/div[3]/div/div[1]/div/div[1]/div/div[1]/div[2]/h3
# food name: /html/body/div[2]/div/div[2]/div[3]/div/div[2]/div/div[2]/div/div[1]/div[1]/h3
# food price: /html/body/div[2]/div/div[2]/div[3]/div/div[2]/div/div[2]/div/div[1]/div[1]/div/div/span
# /html/body/div[2]/div/div[2]/div[4]/div/div[1]/div/div[1]/div/div/div[1]/div
