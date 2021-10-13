from selenium import webdriver
import pytest
from pages.login_page import *
from pages.Homepage import *
class Test_login:
    @pytest.fixture(scope="class")
    def test_setup(self):
        global driver
        driver =webdriver.Chrome("../drivers/chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(3)
        yield
        driver.close()
        driver.quit()

    def test_login(self,test_setup):
        login = loginpage(driver)
        login.txt_username_id("Admin")
        login.txt_password_id("admin123")
        login.click_login()


    def test_logout(self,test_setup):
        homepage = Homepage(driver)
        homepage.click_welcome()
        homepage.click_logout()

