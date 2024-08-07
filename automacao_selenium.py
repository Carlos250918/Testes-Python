from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()
chrome.get('https://books.toscrape.com/')
sleep(1)
book = chrome.find_element(By .XPATH,'/html/body/div/div/div/div/section/div[2]/ol/li[1]/article/h3/a')

titulo = chrome.find_element(By.XPATH,'/html/body/div/div/div[2]/div[2]/article/div[1]/div[2]/h1')
print(titulo.get_attribute('title'))


sleep(10)