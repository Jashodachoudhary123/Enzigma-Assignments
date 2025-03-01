#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import unittest

class LoginPageValidation:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # WebDriverWait with a 10-second timeout
    
    def find_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def validate_login(self, username, password):
        # Find the username, password fields, and login button
        username_field = self.find_element(By.XPATH, "//input[@name='username']")
        password_field = self.find_element(By.XPATH, "//input[@autocomplete='new-password']")
        login_button = self.find_element(By.XPATH, "//*[@title='Log In']")
        error_message = self.find_element(By.XPATH, "//*[contains(text(),'Invalid username or password')]")
        
        # Enter username and password
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Click the login button
        login_button.click()

        # Validation
        if username == "validUser" and password == "validPass":
            # Wait for the dashboard page or URL validation
            self.wait.until(EC.url_contains("dashboard"))
            assert "dashboard" in self.driver.current_url, "Login failed!"
        else:
            # Wait for the error message to appear
            self.wait.until(EC.visibility_of(error_message))
            assert error_message.is_displayed(), "Error message not displayed for invalid login!"


# In[ ]:




