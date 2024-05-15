import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def find_cheapest_flight():
    driver = webdriver.Chrome()

    driver.get("https://www.google.com/travel/flights.com")  # Replace "example.com" with the actual website you prefer to use
    
    # EXAMPLE: I used this script to search for the flight from Luxembourg to Milan, feel free to change
    search_origin = driver.find_element_by_id("origin-input")
    search_origin.send_keys("Luxembourg")
    
    search_destination = driver.find_element_by_id("destination-input")
    search_destination.send_keys("Milan")
    
    search_button = driver.find_element_by_id("search-button")
    search_button.click()
    time.sleep(5)
    
    flight_prices = driver.find_elements_by_class_name("flight-price")  # Replace "flight-price" with the correct selector for flight prices on the website you are using
    
    cheapest_price = float('inf')
    for price in flight_prices:
        price_value = float(price.text.replace('€', '').replace(',', ''))
        if price_value < cheapest_price:
            cheapest_price = price_value
    

    purchase_button = driver.find_element_by_id("purchase-button")  # Replace "purchase-button" with the correct selector for the purchase button on the website you are using
    purchase_button.click()
    

    driver.quit()

find_cheapest_flight()