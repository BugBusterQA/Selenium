"""
2024 (c) QA Automation
"""
from selenium.webdriver.common.by import By


def test_smoke(browser):
    """
    SMK-1. Smoke test
    """
    browser.get("https://demoqa.com/text-box")

    button = browser.find_element(By.ID, "submit")
    assert button.text == "Submit", "Button text is incorrect"

def test_empty_input_send(browser):
    """
    SMK-2. Negative case: empty input send
    """
    browser.get("https://www.saucedemo.com/")

    email_input_name = browser.find_element(By.ID, "user-name")
    email_input_pass = browser.find_element(By.ID, "password")
    
    button = browser.find_element(By.ID, "login-button")
    button.click()

    email_error_label = browser.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')

    assert email_error_label.get_attribute('innerText') == "Epic sadface: Username is required", "empty input has been sent, but it shouldn't have been"

def test_correct_input_send(browser):
    """
    SMK-3. Positive case: correct input send
    """
    browser.get("https://www.saucedemo.com/")

    email_input_name = browser.find_element(By.ID, "user-name")
    email_input_pass = browser.find_element(By.ID, "password")

    email_input_name.send_keys("standard_user")
    email_input_pass.send_keys("secret_sauce")
    
    button = browser.find_element(By.ID, "login-button")
    button.click()

    assert browser.current_url == "https://www.saucedemo.com/inventory.html", "correct input hasn't been sent"
