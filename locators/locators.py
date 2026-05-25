
from selenium.webdriver.common.by import By

class Locators:

 reglog_button = (By.XPATH, "//button[contains(text(),'Вход и регистрация')]")
 no_account_button = (By.XPATH, "//button[contains(text(),'Нет аккаунта')]")
 email_placeholder = (By.NAME, 'email')
 password_placeholder = (By.NAME, 'password')
 password_submit_placeholder = (By.NAME, 'submitPassword')
 create_account_button = (By.XPATH, "//button[contains(text(),'Создать аккаунт')]")
 error_message = (By.XPATH, "//span[contains(text(),'Ошибка')]")
 enter_login_button = (By.XPATH, "//button[contains(text(),'Войти')]")
 logout_button = (By.XPATH, "//button[contains(text(),'Выйти')]")
 create_announcement_button = (By.XPATH, "//button[contains(text(),'Разместить объявление')]")
 title_placeholder =(By.NAME, 'name')
 category_dropdown = (By.CSS_SELECTOR, "input[value='Авто']")
 condition_new_radio = (By.XPATH, "//input[@name='condition'][@value='Новый']")
 condition_used_radio = (By.XPATH, "//input[@name='condition'][@value='Б/У']")
 city_dropdown = (By.XPATH, "//input[@name='city']")
 choose_city_ekaterinburg = (By.XPATH, "(//button[@type='button'])[16]")
 description_placeholder = (By.TAG_NAME, "textarea")
 price_placeholder = (By.NAME, 'price')
 submit_announcement_button = (By.CSS_SELECTOR, "button[type='submit']")
 authorization_notification_title = (By.CSS_SELECTOR, ".h1")