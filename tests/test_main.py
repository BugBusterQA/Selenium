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
