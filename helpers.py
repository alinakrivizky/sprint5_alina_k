
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def select_dropdown_option(driver, dropdown_locator, option_text, wait_time=10):
    wait = WebDriverWait(driver, wait_time)
    dropdown = wait.until(EC.element_to_be_clickable(dropdown_locator))
    driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
    dropdown.click()
    script = f"""
    const buttons = Array.from(document.querySelectorAll('.dropDownMenu_btn__o8ARs'));
    const option = buttons.find(btn => btn.textContent.includes('{option_text}'));
    if (option) {{
        option.click();
        return true;
    }}
    return false;
    """
    result = driver.execute_script(script)
    if not result:
        raise Exception(f"Could not find dropdown option with text: {option_text}")


def click_radio_button(driver, radio_locator, wait_time=10):
    wait = WebDriverWait(driver, wait_time)
    radio = wait.until(EC.presence_of_element_located(radio_locator))
    driver.execute_script("arguments[0].click();", radio)

