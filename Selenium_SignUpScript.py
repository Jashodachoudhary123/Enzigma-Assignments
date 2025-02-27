from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set Chrome Driver Path (Update if needed)
chrome_driver_path = "C:\\Users\\91878\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

# Initialize Chrome WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Open NoKodr Signup Page
    url = "https://app-staging.nokodr.com/"
    print(f"Opening {url}")
    driver.get(url)
    driver.maximize_window()

    # Wait for 'Sign Up' button and click
    signup_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Sign up']"))
    )
    signup_button.click()
    print("✅ Signup popup opened")

    # Wait for the signup form to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//form"))
    )
    print("✅ Signup form loaded")

    # Locate all input fields (using proper XPath)
    name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='fullName' or @placeholder='Full Name']"))
    )
    email_input = driver.find_element(By.XPATH, "//input[@name='username' or @type='email']")
    password_input = driver.find_element(By.XPATH, "//input[@name='password']")
    confirm_password_input = driver.find_element(By.XPATH, "//input[@name='confirmPassword']")
    submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Sign Up')]")

    # **Test Case 1: Valid Signup**
    print("▶ Entering valid signup data...")
    name_input.clear()
    name_input.send_keys("Test User")
    
    email_input.clear()
    email_input.send_keys("testuser@example.com")
    
    password_input.clear()
    password_input.send_keys("Test@1234")
    
    confirm_password_input.clear()
    confirm_password_input.send_keys("Test@1234")

    submit_button.click()
    print("✅ Submitted signup form")

    # Validate success message
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Account created successfully')]"))
    )
    assert success_message.is_displayed(), "Signup failed with valid data!"
    print("🎉 Signup successful!")

    time.sleep(3)  # Pause before next test

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    time.sleep(3)
    print("Closing the browser")
    driver.quit()
