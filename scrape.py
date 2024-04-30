from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

def scrape(search_query):
    # Setup WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in background
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(f'https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText={search_query}')

    # Wait for JavaScript to load
    time.sleep(5)  # Adjust time based on your connection speed and response time of the website

    # Extract data
    products = []
    # Note: The class names used below are placeholders and must be replaced with actual values from Alibaba
    items = driver.find_elements(By.CSS_SELECTOR, '.m-gallery-product-item-v2')
    for item in items:
        try:
            title = item.find_element(By.CSS_SELECTOR, '.elements-title-normal__outter').text
            price = item.find_element(By.CSS_SELECTOR, '.elements-offer-price-normal__price').text
            description = "Not always available"  # Example placeholder if specific descriptions are not uniformly available
            image = item.find_element(By.CSS_SELECTOR, 'img').get_attribute('src')

            products.append({
                'Title': title,
                'Price': price,
                'Description': description,
                'Image': image
            })
        except Exception as e:
            print(f'Error extracting item details: {e}')
            continue

    # Close the browser
    driver.quit()

    # Convert to DataFrame
    df = pd.DataFrame(products)
    return df

