import csv
import time
from itertools import product

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
url = "https://www.divan.ru/category/svet"
driver.get(url)
time.sleep(3)

products = driver.find_elements(By.CSS_SELECTOR, 'product--ui-OCRn7 BreadcrumbLink')

print(products)

parsed_data = []

for product in products:
    try:
        name = product.find_element(By.CSS_SELECTOR, 'h1.DqOqS').text
        price = product.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU JIybk').text
        link = product.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
    except:
        print("Произошла ошибка при парсинге.")
    continue

    parsed_data.append({'name': name, 'price': price, 'link': link})


with open('lighting.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['name', 'price', 'link']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in data:
        writer.writerow(row)

driver.quit()