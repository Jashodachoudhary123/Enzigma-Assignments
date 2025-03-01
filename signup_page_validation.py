#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class SignupPageValidation:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # WebDriverWait with a 10-second timeout
    
    def find_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def validate_signup(self, email):
        # Find the signup button, email field, proceed button, and success message
        signup_button = self.find_element(By.XPATH, "//*[@class='slds-float_right']/a")
        email_field = self.find_element(By.XPATH, "//*[@id='id_17364210188447499']")
        proceed_button = self.find_element(By.XPATH, "//*[@id='modal-content-id-1']/abx-sign-up/div/div/div[2]/span/div[2]/abx-button/button")
        success_message = self.find_element(By.XPATH, "//*[contains(text(),'Account created successfully!')]")
        
        # Click the signup button
        signup_button.click()

        # Enter the email in the email field
        email_field.send_keys(email)

        # Click the proceed button
        proceed_button.click()

        # Wait for the success message and validate
        self.wait.until(EC.visibility_of(success_message))
        assert success_message.text == "Account created successfully!", "Signup failed!"


# In[ ]:




