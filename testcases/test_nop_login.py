from pageobjects.nop_login import Nop_login
from utilities.readproperity import ReadConfig
from utilities.customlogger import LogGen


class Test_nop_Login:
    url = ReadConfig.get_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    expected_title = 'Dashboard / nopCommerce administration'

    def test_login(self, setup):
        self.logger.info('************** test_ login nop started')
        self.driver = setup
        self.logger.info('***** opening url***')
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.lp = Nop_login(self.driver)
        self.logger.info('-------------- sending username')
        self.lp.set_username(self.username)
        self.logger.info('----- entering password')
        self.lp.set_password(self.password)
        self.logger.info('____ click on login')
        self.lp.click_login()
        self.logger.info('verifying the title ')
        self.lp.verify_login(self.expected_title)
        self.logger.info('click logout button')
        self.lp.click_logout()
        self.driver.save_screenshot('.\\screenshots\\test_nop_loin.png')
        self.logger.info('program is passed')
