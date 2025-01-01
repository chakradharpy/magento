## Overview
This project automates the signup flow on the Magento e-commerce platform using Selenium and Pytest frameworks. The project adheres to Page Object Model (POM). Test data is read dynamically from an Excel sheet .

---

## Folder Structure

```
|-- exceldata
|   |-- sigunp_data.xlsx  # Test data for signup tests
|-- locators
|   |-- locator.py        # Locator definitions for the signup page
|-- pages
|   |-- signup.py         # Page object implementation for signup functionalities
|   |-- readexcel.py      # Utility to read data from Excel files
|-- utils
|   |-- logger.py         # Logger utility for better debugging and reporting
|-- conftest.py           # Pytest fixtures and setup
|-- requirements.txt      # Required dependencies for the project
|-- README.md             # Project documentation
| --test_signup.py         # Test cases for signup functionality

|---test_login.py          # Test cases for login functionality

---

## Prerequisites
Ensure you have the following installed:
1. Python 3.8+
2. Pip (Python package installer)

---

## Installation
1. Clone the repository:
    git clone <repository_url>
    cd <repository_name>
    ```

2. Create a virtual environment:
    python -m venv venv
    venv\Scripts\activate   # For Windows
    ```

3. Install dependencies:
    pip install -r requirements.txt
    ```

4. Place the `sigunp_data.xlsx` file in the `exceldata` directory.

---

## How to Run the Tests
1. Execute all test cases:
    pytest -v
    ```
`

3. Run specific tests:
    pytest -k "test_name"
    ```
