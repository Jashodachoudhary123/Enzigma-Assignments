#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import unittest
from forgot_password_validation import ForgotPasswordValidation  # Correct import
from base_test import BaseTest  # Correct import

class ForgotPasswordTest(BaseTest):

    def test_forgot_password(self):
        # Instantiate the ForgotPasswordValidation class
        forgot_password = ForgotPasswordValidation(self.driver)
        # Call the validate_forgot_password method with the test email
        forgot_password.validate_forgot_password("testemail@example.com")

if __name__ == "__main__":
    unittest.main()  # This runs the test


# In[ ]:




