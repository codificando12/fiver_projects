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
import time

def run():

    driver = webdriver.Chrome(executable_path= r'C:/chrome-driver/chromedriver.exe')
    driver.get('https://gofood.co.id/jakarta/restaurants/near-me?page=1')
    driver.maximize_window()

    for restaurant in range(1, 31):
        try:
            shop = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, f'//*[@id="__next"]/div/div[3]/div[1]/div[{restaurant}]/a')))
        except:
            driver.execute_script("window.scrollBy(0, 2000);")
            shop = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, f'//*[@id="__next"]/div/div[3]/div[1]/div[{restaurant}]/a')))
        shop.click()
        items = 0
        while items < 3:
            rest_name = WebDriverWait(driver,10).until(EC.presence_of_element_located(
                (By.XPATH, ' //*[@id="__next"]/div/div[2]/div[1]/div[1]/div[1]/div[1]/h1')))
            loc_distance = WebDriverWait(driver,10).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/div[2]/div/div[2]/div/p')))
            loc_city =  WebDriverWait(driver,10).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/div[2]/div/div[2]/p')))
            print("restaurant: " + rest_name.text)
            print(f"location: {loc_city.text} {loc_distance.text}")
            print(driver.current_url)
            items += 1
            time.sleep(3)
        driver.back()
        print(restaurant)
    driver.close()
if __name__ == "__main__":
    run()


# /html/body/div[2]/div/div[2]/div[3]/div/div[1]/div/div
# /html/body/div[2]/div/div[2]/div[3]/div/div[2]/div/div[1]
# /html/body/div[2]/div/div[2]/div[3]/div/div[1]/div/div[1]