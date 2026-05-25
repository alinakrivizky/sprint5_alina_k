
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from ..locators.locators import Locators

@pytest.fixture(scope='function')
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get('https://qa-desk.education-services.ru/')
    
    yield driver
    
    driver.quit()


@pytest.fixture(scope='function')
def logged_in_user(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable(Locators.reglog_button)).click()
    wait.until(EC.url_contains("/login"))
    
    email = wait.until(EC.element_to_be_clickable(Locators.email_placeholder))
    email.click()
    email.send_keys("al@gmail.com")
    
    password = wait.until(EC.element_to_be_clickable(Locators.password_placeholder))
    password.click()
    password.send_keys("aaaaaddddd12R")
    
    wait.until(EC.element_to_be_clickable(Locators.enter_login_button)).click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".profileText.name")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".svgSmall")))
    
    return driver


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

