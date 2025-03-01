#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install selenium


# In[8]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

class BaseTest:
    def __init__(self):
        self.driver = None

    def setup(self):
        # Setup Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")  # Maximize the window

        # Initialize the WebDriver
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  # Wait for elements to load
        self.driver.get("https://app-staging.nokodr.com/")  # Open the URL

    def teardown(self):
        if self.driver:
            self.driver.quit()  # Close the browser

    def run_test(self):
        self.setup()  # Start the setup (open browser, maximize window, etc.)
        
        # Perform any test actions here (for example, interacting with a page)
        # You can also wait for elements, click, type, etc.
        time.sleep(2)  # Just for demonstration purposes, wait for 2 seconds
        
        # Call the teardown to close the browser after the test
        self.teardown()

if __name__ == "__main__":
    test = BaseTest()
    test.run_test()  # Run the test


# In[ ]:




