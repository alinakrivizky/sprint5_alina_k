

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sprint_5.locators.locators import Locators
from sprint_5.helpers import select_dropdown_option, click_radio_button
import time


class TestAnnouncement:
    def test_create_announcement_by_logged_in_user(self, logged_in_user):
        driver = logged_in_user
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(Locators.create_announcement_button)).click()
        wait.until(EC.presence_of_element_located(Locators.title_placeholder))
        title = wait.until(EC.element_to_be_clickable(Locators.title_placeholder))
        title.click()
        title.send_keys("Test Announcement")
        
        select_dropdown_option(driver, Locators.category_dropdown, "Книги")
        wait.until(EC.element_to_be_clickable(Locators.condition_used_radio))
        click_radio_button(driver, Locators.condition_used_radio)
        wait.until(
            lambda d: "radioUnput_inputActive" in d.find_element(*Locators.condition_used_radio).get_attribute("class")
        )

        select_dropdown_option(driver, Locators.city_dropdown, "Екатеринбург")
        wait.until(EC.element_to_be_clickable(Locators.description_placeholder))
        
        description = wait.until(EC.element_to_be_clickable(Locators.description_placeholder))
        description.click()
        description.send_keys("This is a test announcement created by an automated test.")
        wait.until(EC.presence_of_element_located(Locators.price_placeholder))
        price = wait.until(EC.element_to_be_clickable(Locators.price_placeholder))
        price.click()
        price.send_keys("1000")
        wait.until(EC.element_to_be_clickable(Locators.submit_announcement_button)).click()

        assert "/create-lisiting" in driver.current_url
        time.sleep(2)  

    def test_create_announcement_by_unregistered_user(self, driver):
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(Locators.create_announcement_button)).click()
        wait.until(EC.presence_of_element_located(Locators.authorization_notification_title))
        notification_title = wait.until(EC.visibility_of_element_located(Locators.authorization_notification_title))
        assert notification_title.text == "Чтобы разместить объявление, авторизуйтесь"
