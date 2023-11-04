# RPA robot process automatization
# use cases: web scraping, test automation.
# powered by selenium

from selenium import webdriver # web driver
from selenium.webdriver.chrome.service import Service as ServiceChrome # service chrome
from selenium.webdriver.edge.service import Service as ServiceEdge
from selenium.webdriver.common.by import By  # search strategy
from selenium.webdriver.common.action_chains import ActionChains # mouse actions
import time # time module

serviceChrome = ServiceChrome('driver/chromedriver.exe')
serviceEdge = ServiceEdge('driver/msedgedriver.exe')

SEARCH_PARAM = 'ps5'

def serviceSelect(explorer='chrome'):
    if explorer == 'edge':
        return webdriver.Edge(service=serviceEdge)
    return webdriver.Chrome(service=serviceChrome)

driver = serviceSelect(explorer='edge')
driver.maximize_window()
time.sleep(1)
driver.get('https://www.mercadolibre.com.co')
time.sleep(1)
searchBar = driver.find_element(By.XPATH, '/html/body/header/div/div[2]/form/input' )
time.sleep(1)
searchBar.click()
time.sleep(1)
searchBar.send_keys(SEARCH_PARAM)
time.sleep(1)
searchBar.submit()
time.sleep(2)


# scrap one page of products in mercadolibre

productList = driver.find_elements(By.XPATH, '/html/body/main/div/div[2]/section/ol/li')
time.sleep(1)
for product in productList:
    product_destructured = product.text.split('\n')
    # print(product_destructured)
    print(f'Name: {product_destructured[0] if product_destructured[0] != "MÁS VENDIDO" else  product_destructured[1]}')
    print(f'Price: {product_destructured[2] if product_destructured[2] != "$" else product_destructured[3]}')
    print('-----------------------')