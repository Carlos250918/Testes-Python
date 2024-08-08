from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


chrome = webdriver.Chrome()
chrome.get('https://books.toscrape.com/')
sleep(1)

books = chrome.find_elements(By.XPATH,'//article[@class="product_pod"]')
for book in books:
    title = book.find_element(By.XPATH,'./h3/a')
    title.click ()
    sleep(1)

    preço = chrome.find_element(By.XPATH,'//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    estoque = chrome.find_element(By.XPATH,'//*[@id="content_inner"]/article/div[1]/div[2]/p[2]')
    print(title.text)
    print(preço.text)
    print(estoque.text)

    chrome.back()
sleep(1)

for book in books:
    title = book.find_element(By.XPATH,'//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    title.click()
    sleep(1)
    
