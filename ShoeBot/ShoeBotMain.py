"""exploratory mainn file for building shoe bot"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def kith(url):

    driver = webdriver.Chrome(executable_path="/Users/ep9k/Desktop/ShoeBot/drivers/chromedriver")

    driver.maximize_window() # browser window needs to be large enough for the add cart button to show up
    driver.get(url)
    
    # wait for signup form to become clickable and click the X to close it. This step doesn't have to be in this order, but box pops up eventually anyway.
    wait = WebDriverWait(driver, 10)
    elem = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nike-air-force-1-39-07-low-white"]/div[6]/div/div/div/button/img')))
    elem.click()
    
    # get the add cart button and click it
    #this works
#    elem = driver.find_element_by_xpath('//*[@id="shopify-section-product"]/section[1]/div[4]/form/button')
    #this also works
#    elem = driver.find_element_by_xpath('//*[@class="shopify-section"]/section[1]/div[4]/form/button')
    #this also works
    elem = driver.find_element_by_xpath('//*[@class="product-single__shop"]/form/button')
    elem.click()
    
#    # click checkout button when shopping cart pops up
    #START HERE. NO SUCH ELEMENT EXCEPTION
    elem = driver.find_element_by_xpath('//*[@class="ajaxcart__container"]/form/button')
    elem.click()

kith('https://kith.com/collections/nike-air-force-one-collection/products/nike-air-force-1-07-white')
