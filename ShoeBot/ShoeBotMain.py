"""exploratory mainn file for building shoe bot"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path="/Users/ep9k/Desktop/ShoeBot/drivers/chromedriver")


def kith(url):

#    driver = webdriver.Chrome(executable_path="/Users/ep9k/Desktop/ShoeBot/drivers/chromedriver")

    driver.maximize_window() # browser window needs to be large enough for the add cart button to show up
    driver.get(url)
    
    # wait for signup form to become clickable and click the X to close it. This step doesn't have to be in this order, but box pops up eventually anyway.
#    wait = WebDriverWait(driver, 10)
#    elem = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nike-air-force-1-39-07-low-white"]/div[6]/div/div/div/button/img')))
#    elem.click()
    
    # get the add cart button and click it
    add_to_cart = driver.find_element_by_xpath('//*[@class="product-single__shop"]/form/button')
    add_to_cart.click()
        
#    # click checkout button when shopping cart pops up
    wait = WebDriverWait(driver, 10)
    checkout = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="CartContainer"]/form/div[2]/button')))
    checkout.click()
    
#    autofil shopify checkout template
    shopify_template()

        

def shopify_template():
    """Auto Fill shopify template. This is a common payment template shared by a lot of the shoe sites"""
    
    #fill in email field
    wait = WebDriverWait(driver, 10)
    email_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout_email"]')))
    email_field.send_keys('yuiruprup@hotmail.com')
    
    #unclick 'email me' button below email box
    elem = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout_buyer_accepts_marketing"]')))
    elem.click()
  
    time.sleep(.2)
    
    #fill in shipping address information
    first_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout_shipping_address_first_name"]')))
    first_name.send_keys('Dummy')
    
    time.sleep(.2)
    
    last_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout_shipping_address_last_name"]')))
    last_name.send_keys('Name')
    
    time.sleep(.2)
    
    address = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout_shipping_address_address1"]')))
    address.send_keys('160 McCormick Rd.')
    
    time.sleep(.2)
    
    city = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout_shipping_address_city"]')))
    city.send_keys('Charlottesville')
    
    time.sleep(.2)
    
    state_box = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout_shipping_address_province"]')))
    state_box.click()
    state = Select(driver.find_element_by_xpath('//*[@id="checkout_shipping_address_province"]'))   #must select <select> element. Which is the state
    state.select_by_value('VA')
    
    time.sleep(.2)

    zip_code = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout_shipping_address_zip"]')))
    zip_code.send_keys('22903')
    
    time.sleep(.2)

    phone_number = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout_shipping_address_phone"]')))
    phone_number.send_keys('5558675309')

    #click 'continue to shipping' button
    continue_to_shipping = driver.find_element_by_xpath('//*[@id="continue_button"]')
    continue_to_shipping.click()
    
    ####START HERE

kith('https://kith.com/collections/nike-air-force-one-collection/products/nike-air-force-1-07-white')


###adding some extra comment for github
