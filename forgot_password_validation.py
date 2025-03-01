#!/usr/bin/env python
# coding: utf-8

# In[3]:


from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ForgotPasswordValidation:
    def __init__(self, driver):
        self.driver = driver

    def validate_forgot_password(self, email):
        # Locate the "Forgot Password" link and click it
        forgot_password_link = self.driver.find_element(By.LINK_TEXT, "Forgot your password?")
        forgot_password_link.click()

        # Locate the email input field and submit the provided email
        email_field = self.driver.find_element(By.NAME, "email")
        email_field.send_keys(email)
        email_field.send_keys(Keys.RETURN)  # Submit the form
        
        # Optionally, you can add assertions here to confirm that an email was sent or the page updated.


# In[ ]:





# In[ ]:




