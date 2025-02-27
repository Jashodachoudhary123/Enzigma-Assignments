from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set Chrome Driver Path (replace with your chromedriver path)
chrome_driver_path = "C:\\Users\\91878\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

# Initialize Chrome WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Open the browser and navigate to the NoKodr platform
    url = "https://app-staging.nokodr.com/"
    print(f"Opening {url}")
    driver.get(url)
    
    # Maximize the browser window
    driver.maximize_window()
    
    # Wait for page to load completely (basic static wait for demo purposes)
    time.sleep(5)  # Implicit wait
    
    print("Website opened successfully!")

finally:
    # Close the browser after wait time
    print("Closing the browser")
    driver.quit()
