"""
Title
Python - Need web scraper for dynamic site

Description
I'm looking to build a web scraper on python. Looking to collect item name, price, restaurant information 
(name, merchant id, location). Need at least 3 items were collected for each merchant and minimum 30 
merchants scraped from the site.

From https://gofood.co.id/jakarta/restaurants/near-me?page=1

Need it done within 24 hours with source code
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
        rest_name = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, ' //*[@id="__next"]/div/div[2]/div[1]/div[1]/div[1]/div[1]/h1')))
        print(rest_name.text)
        time.sleep(3)
        driver.back()
        print(restaurant)
    driver.close()
if __name__ == "__main__":
    run()


#     //*[@id="__next"]/div/div[2]/div[1]/div[1]/div[1]/div[1]/h1
#    food= //*[@id="section--0"]
#     //*[@id="section-1dc68fc8-be81-4986-aa15-b8b0497a7db6-2"]/div
    # //*[@id="section-8fda4412-1d46-4653-bc24-6e7884a23f8c-3"]