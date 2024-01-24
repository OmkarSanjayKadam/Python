import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from lxml import etree

from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium import webdriver
link = 'https://letterboxd.com/film/poor-things-2023/'

# response = requests.get(link)
# soup = BeautifulSoup(response.text,'lxml')
# print(response.text )

# print(soup.find('h1',class_='headline-1 js-widont prettify').text)
# print(soup.find('img', class_='image'))
# print(soup.find('div', class_='other').a['href'])
# response = requests.get('https://letterboxd.com/')
# soup1 = BeautifulSoup(response.text,'lxml')
# # print(response.text )
# print(soup1.select_one('.overlay'))
# uc.chrom
# chrome_options = uc.ChromeOptions()
# c
# chrome_options.add_argument('--headless')
# chrome_options.headless = True
# driver = uc.Chrome(options=chrome_options)
# driver.get('https://www2.daad.de/deutschland/studienangebote/international-programmes/en/detail/8516/#tab_costs')
#
# time.sleep(1)
# chrome_options = uc.ChromeOptions()
# chrome_options.headless = False
#
# driver = uc.Chrome(options=chrome_options)
# driver.get('https://letterboxd.com/')
# print(driver.find_element(By.XPATH,'//*[@id="html"]/body/div[7]/div[2]/div[1]/div[2]/div[2]/button[1]/p').click())
# time.sleep(2)
# print(driver.page_source)
# soup = BeautifulSoup(driver.page_source,'lxml')
# print(soup.select('a.frame')[0]['href'])


chrome_options = uc.ChromeOptions()
chrome_options.headless = False
driver = uc.Chrome(options=chrome_options)
driver.get('https://www.carsdirect.com/hyundai/kona?acode=00D40HYS181A0')
print(driver.find_element(By.CSS_SELECTOR,'.cdcPriceValuePrimary').click())
# time.sleep(2)
print(driver.page_source)
soup = BeautifulSoup(driver.page_source,'html.parser')
dom = etree.HTML(str(soup))
print(dom.xpath('//*[@id="mainWrapper"]/div[2]/div/div[1]/div[4]/div[1]'))

