#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import unittest
from selenium import webdriver
from signup_page_validation import SignupPageValidation  # Import the SignupPageValidation class

class TestSignup(unittest.TestCase):

    def setUp(self):
        # Set up WebDriver (Chrome in this case)
        self.driver = webdriver.Chrome(executable_path="path_to_chromedriver")
        self.driver.maximize_window()
        self.driver.get("https://app-staging.nokodr.com/")  # Replace with the actual signup URL

    def test_valid_signup(self):
        signup_page = SignupPageValidation(self.driver)
        signup_page.validate_signup("testemail@example.com")

    def tearDown(self):
        # Close the browser after the test
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()  # Run the tests

