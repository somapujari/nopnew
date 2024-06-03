from selenium import webdriver
from pageobjects.login import Login


class Test_Login:
    url = 'https://demo.guru99.com/test/newtours/'
    username = 'mercury'
    password = 'mercury'
    expected_title = 'Welcome: Mercury Tours'

    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.lp = Login(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login()
        self.lp.verify_test(self.expected_title)



