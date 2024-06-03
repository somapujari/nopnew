from selenium.webdriver.common.by import By


class Nop_login:
    textbox_username_id = 'Email'
    textbox_password_id = 'Password'
    button_login_xpath = "//button[@type='submit']"
    text_logout_xpath = '//a[@href="/logout"]'

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.text_logout_xpath).click()

    def verify_login(self, expected_title):
        if self.driver.title == expected_title:
            assert True
        else:
            assert False
