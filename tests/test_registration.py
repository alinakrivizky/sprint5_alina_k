from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sprint_5.locators.locators import Locators
from sprint_5.data import INVALID_EMAIL, NEW_USER_EMAIL_FORMAT, VALID_USER_EMAIL, VALID_USER_PASSWORD

import time


class TestRegistration:
    def test_registration_new_user(self, driver):
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(Locators.reglog_button)).click()
        wait.until(EC.url_contains("/login"))
        wait.until(EC.element_to_be_clickable(Locators.no_account_button)).click()

        wait.until(EC.presence_of_element_located(Locators.email_placeholder))
        email = wait.until(EC.element_to_be_clickable(Locators.email_placeholder))
        email.click()
        random_email = NEW_USER_EMAIL_FORMAT.format(timestamp=int(time.time()))
        email.send_keys(random_email)

        password = wait.until(EC.element_to_be_clickable(Locators.password_placeholder))
        password.click()
        password.send_keys(VALID_USER_PASSWORD)

        confirm = wait.until(EC.element_to_be_clickable(Locators.password_submit_placeholder))
        confirm.click()
        confirm.send_keys(VALID_USER_PASSWORD)

        wait.until(EC.element_to_be_clickable(Locators.create_account_button)).click()
        profile_name = wait.until(EC.visibility_of_element_located(Locators.profile_name))
        profile_icon = wait.until(EC.visibility_of_element_located(Locators.profile_icon))
        assert profile_name.is_displayed(), "Profile name should be visible after registration"
        assert profile_icon.is_displayed(), "Profile icon should be visible after registration"

    def test_registration_with_invalid_email(self, driver): 
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(Locators.reglog_button)).click()
        wait.until(EC.url_contains("/login"))
        wait.until(EC.element_to_be_clickable(Locators.no_account_button)).click()

        wait.until(EC.presence_of_element_located(Locators.email_placeholder))
        email = wait.until(EC.element_to_be_clickable(Locators.email_placeholder))
        email.click()
        email.send_keys(INVALID_EMAIL)

        password = wait.until(EC.element_to_be_clickable(Locators.password_placeholder))
        password.click()
        password.send_keys(VALID_USER_PASSWORD)

        confirm = wait.until(EC.element_to_be_clickable(Locators.password_submit_placeholder))
        confirm.click()
        confirm.send_keys(VALID_USER_PASSWORD)
        
        wait.until(EC.element_to_be_clickable(Locators.create_account_button)).click()
        error_message = wait.until(EC.visibility_of_element_located(Locators.error_message))
        assert error_message.text == "Ошибка", f"Expected 'Ошибка', but got '{error_message.text}'"

    def test_registration_already_registered_user(self, driver):
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(Locators.reglog_button)).click()
        wait.until(EC.url_contains("/login"))
        wait.until(EC.element_to_be_clickable(Locators.no_account_button)).click()

        wait.until(EC.presence_of_element_located(Locators.email_placeholder))
        email = wait.until(EC.element_to_be_clickable(Locators.email_placeholder))
        email.click()
        email.send_keys(VALID_USER_EMAIL)
        password = wait.until(EC.element_to_be_clickable(Locators.password_placeholder))
        password.click()
        password.send_keys(VALID_USER_PASSWORD)
        confirm = wait.until(EC.element_to_be_clickable(Locators.password_submit_placeholder))
        confirm.click()
        confirm.send_keys(VALID_USER_PASSWORD)
        wait.until(EC.element_to_be_clickable(Locators.create_account_button)).click()
        error_message = wait.until(EC.visibility_of_element_located(Locators.error_message))
        assert error_message.text == "Ошибка", f"Expected 'Ошибка', but got '{error_message.text}'"
