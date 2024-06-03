from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:
    username_input_name = 'userName'
    password_inp_name = 'password'
    submit_btn_name = 'submit'

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.NAME, self.username_input_name).clear()
        self.driver.find_element(By.NAME, self.username_input_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.password_inp_name).clear()
        self.driver.find_element(By.NAME, self.password_inp_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.NAME, self.submit_btn_name).click()
        print(self.driver.title)

    # def verify_test(self, expected_title):
    #     print(self.driver.title)
    #     if expected_title in self.driver.title:
    #         assert True
    #     else:
    #         assert False

    # def verify_test(self, expected_title):
    #     WebDriverWait(self.driver, 10).until(EC.title_contains(expected_title))
    #     actual_title = self.driver.title
    #     assert expected_title in actual_title, f"Expected '{expected_title}' in title, but got '{actual_title}'"
    #
    def verify_test(self, expected_title):
        try:
            print(f"Waiting for title to contain: {expected_title}")
            WebDriverWait(self.driver, 10).until(EC.title_contains(expected_title))
            actual_title = self.driver.title
            print(f"Actual title: {actual_title}")
            assert expected_title in actual_title, f"Expected '{expected_title}' in title, but got '{actual_title}'"
        except TimeoutException:
            actual_title = self.driver.title
            print(f"Timeout occurred. Actual title: {actual_title}")
            assert False, f"Expected '{expected_title}' in title, but got '{actual_title}'"