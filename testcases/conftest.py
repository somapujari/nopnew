from selenium import webdriver
import pytest


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    yield driver
    driver.delete_all_cookies()
    driver.quit()
