#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import unittest
from selenium import webdriver
from login_page_validation import LoginPageValidation  # Importing the LoginPageValidation class

class TestLogin(unittest.TestCase):

    def setUp(self):
        # Set up WebDriver (Chrome in this case)
        self.driver = webdriver.Chrome(executable_path="path_to_chromedriver")
        self.driver.maximize_window()
        self.driver.get("https://app-staging.nokodr.com/")  # Replace with actual login URL

    def test_valid_login(self):
        login_page = LoginPageValidation(self.driver)
        login_page.validate_login("validUser", "validPass")

    def test_invalid_login(self):
        login_page = LoginPageValidation(self.driver)
        login_page.validate_login("invalidUser", "invalidPass")

    def tearDown(self):
        # Close the browser after the test
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()  # Run the tests

