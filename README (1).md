# NoKodr Automation Testing Scripts

This repository contains Selenium WebDriver automation scripts for testing various functionalities of the NoKodr platform. The scripts are written in Python and demonstrate how to automate basic browser interactions, signup page validation, and login page validation.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Scripts Description](#scripts-description)
  - [1. Basic Script](#1-basic-script)
  - [2. Signup Page Validation](#2-signup-page-validation)
  - [3. Login Page Validation](#3-login-page-validation)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Overview

These scripts automate key user interactions on the NoKodr platform:
- **Basic Script:** Opens a browser (Chrome) and navigates to the NoKodr staging environment.
- **Signup Page Validation:** Automates the signup process by validating input fields, submitting the form, and verifying success or error messages.
- **Login Page Validation:** Automates the login process by entering credentials, interacting with dynamic elements (like the password "Show" button), and verifying the outcome.

## Prerequisites

Before running these scripts, ensure you have the following installed:
- **Python 3.7+**
- **Google Chrome** (latest version recommended)
- **ChromeDriver:** Download the correct version from [ChromeDriver Download](https://sites.google.com/chromium.org/driver/) and update the path in the scripts.
- **Selenium Package:** Install via pip:
  ```bash
  pip install selenium
