from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sprint_5.locators.locators import Locators



def test_login_valid_user(driver):
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
    profile_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".profileText.name")))
    profile_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".svgSmall")))
    assert profile_name.is_displayed(), "Profile name should be visible after login"
    assert profile_icon.is_displayed(), "Profile icon should be visible after login"



def test_logout_already_logged_in_user(logged_in_user):
    driver = logged_in_user
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable(Locators.logout_button)).click()
    reglog_button = wait.until(EC.visibility_of_element_located(Locators.reglog_button))
    assert reglog_button.is_displayed(), "Login/Registration button should be visible after logout"
