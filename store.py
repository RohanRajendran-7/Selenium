from datetime import timedelta,datetime
from selenium import webdriver
# import openpyxl
import os
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common import keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support.ui import Select
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

search_term = input()
search_term = search_term.replace(" ","+")
print(search_term)
search_query = "https://www.amazon.in/s?k="+search_term+""
print(search_query)
driver.get(search_query)
driver.maximize_window()

# lst = driver.find_elements(By.XPATH,"//div[@data-component-type='s-search-result']")
# count = 1
result_list = []
# record = {}
# for i in lst:
#     price = driver.find_element(By.XPATH,"(//div[@data-component-type='s-search-result']//span[@class='a-price-whole'])["+str(count)+"]").text
#     record["price"] = price
#     name = driver.find_element(By.XPATH,"(//div[@data-component-type='s-search-result']//h5)["+str(count)+"]").text
#     record["name"] = name
#     description = driver.find_element(By.XPATH,"(//div[@data-component-type='s-search-result']//h2)["+str(count)+"]").text
#     record["description"] = description
#     # rating = driver.find_element(By.XPATH,"(//div[@data-component-type='s-search-result']//span[@class='a-icon-alt'])["+str(count)+"]").text
#     # rating = rating.split(" ")[0]
#     # record["rating"] = rating
#     img_src = driver.find_element(By.XPATH, "(//div[@data-component-type='s-search-result']//img[@class='s-image'])["+str(count)+"]").get_attribute("src")
#     record["img"] = img_src
#     print(record)
#     result_list.append(record.copy())
#     count += 1
# print(result_list)

# driver.get("https://www.ajio.com/search/?text="+search_term+"")
# for count in range(1,45):
#     element = driver.find_element(By.XPATH,"(//div[@class='imgHolder']//img[@class='rilrtl-lazy-img  rilrtl-lazy-img-loaded'])["+str(count)+"]")
#     driver.execute_script("arguments[0].scrollIntoView();", element)
#     img_text = driver.find_element(By.XPATH,"(//div[@class='imgHolder']//img[@class='rilrtl-lazy-img  rilrtl-lazy-img-loaded'])["+str(count)+"]").get_attribute("src")
#     record["img"] = img_text
#     name = driver.find_element(By.XPATH, "(//div[@class='contentHolder']//div[@class='brand'])["+str(count)+"]").text
#     record["name"] = name
#     description = driver.find_element(By.XPATH, "(//div[@class='contentHolder']//div[@class='nameCls'])["+str(count)+"]").text
#     record["description"] = description
#     price = driver.find_element(By.XPATH, "(//div[@class='contentHolder']//span[@class='price  '])["+str(count)+"]").text
#     record["price"]  = price
#     result_list.append(record.copy())
# print(result_list)
driver.get("https://www.myntra.com/"+search_term+"")
lst = driver.find_elements(By.XPATH,"//li[@class='product-base']")

count = 1
record = {}
for i in lst:
    element = driver.find_element(By.XPATH,"(//picture[@class='img-responsive']//img)["+str(count)+"]")
    driver.execute_script("arguments[0].scrollIntoView();",element)
    img_src = driver.find_element(By.XPATH, "(//picture[@class='img-responsive']//img)["+str(count)+"]").get_attribute("src")
    record["img"] = img_src
    name = driver.find_element(By.XPATH, "(//li[@class='product-base']//h3[@class='product-brand'])["+str(count)+"]").text
    record["name"] = name
    description = driver.find_element(By.XPATH, "(//li[@class='product-base']//h4[@class='product-product'])["+str(count)+"]").text
    record["description"] = description 
    try:
        price = driver.find_element(By.XPATH, "(//li[@class='product-base']//span[@class='product-discountedPrice'])["+str(count)+"]").text
        record["price"] = price 
    except NoSuchElementException:
        print("exception")
        price = driver.find_element(By.XPATH, "(//li[@class='product-base']//div[@class='product-price'])["+str(count)+"]").text
        record["price"] = price
    count += 1
    print(record)