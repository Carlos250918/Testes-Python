from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()
chrome.get('https://books.toscrape.com/')
sleep(1)

titulo = chrome.find_element(By.XPATH,'../../media/cache/fe/72/fe72f0532301ec28892ae79a629a293c.jpg' alt="A Light in the Attic">)
print(titulo.get_attribute('title'))

sleep(10)