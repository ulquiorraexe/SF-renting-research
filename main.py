import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import lxml

RENT_URL = "https://appbrewery.github.io/Zillow-Clone/"
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdCNlMEx05orCAef6tafdJqp8vzzcXT4wNRGQUKDpexyEga2A/viewform?usp=sf_link"

response = requests.get(RENT_URL)
soup = BeautifulSoup(response.text, "lxml")

addresses = soup.find_all("a", class_="StyledPropertyCardDataArea-anchor")
prices = soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")
links = soup.find_all("div",class_="StyledPropertyCardPhotoBody")

address_list = []
price_list = []
link_list = []

for address, price, link in zip(addresses, prices, links):
    address_list.append(address.get_text().strip("\n "))
    price_list.append(price.get_text().strip("+/mo"))
    link_list.append(link.find("a")["href"])

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for i in range(len(address_list)):
    driver.get(FORM_URL)
    time.sleep(2)

    address_input = driver.find_element(by=By.XPATH,
                                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element(By.XPATH,
                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element(By.XPATH,
                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    address_input.send_keys(address_list[i])
    time.sleep(1)
    price_input.send_keys(price_list[i])
    time.sleep(1)
    link_input.send_keys(link_list[i])
    time.sleep(1)
    send_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    send_button.click()
    time.sleep(1)

driver.quit()