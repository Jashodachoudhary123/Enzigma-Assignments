from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set Chrome Driver Path
chrome_driver_path = "C:\Users\91878\Downloads\chromedriver-win64\chromedriver-win64.exe"

# Initialize Chrome WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Open the NoKodr Login Page
    url = "https://app-staging.nokodr.com/"
    print(f"Opening {url}")
    driver.get(url)
    driver.maximize_window()

    # Wait for Username Field
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "username"))
    )
    email_input = driver.find_element(By.NAME, "username")
    email_input.clear()
    email_input.send_keys("testuser@example.com")
    print("Email entered successfully")

    # Click Show Password Button (Eye Icon) 🔥
    show_password_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "showButton"))
    )
    show_password_button.click()
    print("Show Password Button Clicked")

    # Wait for Password Field
    password_input = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.NAME, "password"))
    )

    # Use JS to Enable Password Field
    driver.execute_script("arguments[0].removeAttribute('readonly');", password_input)
    driver.execute_script("arguments[0].style.visibility='visible';", password_input)

    password_input.send_keys("Test@123")
    print("Password entered successfully")

    # Click Login Button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Proceed')]"))
    )
    login_button.click()
    print("Login button clicked")

    # Verify Success or Error
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Dashboard')]"))
        )
        print("✅ Login Successful: Dashboard Loaded")
    except:
        print("❌ Login Failed: Invalid Credentials")

finally:
    time.sleep(3)
    print("Closing the browser")
    driver.quit()
