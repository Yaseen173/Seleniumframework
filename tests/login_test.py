from selenium import webdriver
import pytest
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils
import pytest_html
import time
import allure
import moment


@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)
        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_onLogin_button()


    def test_logout(self):
        try:
            driver = self.driver
            homepage = HomePage(driver)
            time.sleep(2)
            homepage.click_on_welcomedrpdwn()
            time.sleep(2)
            homepage.click_on_logout_button()
            x = driver.title
            assert x == 'OrangeHRM'
        except AssertionError:
            print('I knew my Mistake')
            currenttime = moment.now().strftime("%H-%M-%S_%d-%m_%Y")
            testname = utils.whoami()
            screenshot = testname+ "_"+ currenttime
            allure.attach(self.driver.get_screenshot_as_png(),name=screenshot, attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file('C:\\Users\\Muhammad.yaseen\\PycharmProjects\\Workspace_python\\Seleniumframework\\screenshots '+ screenshot + " .png")
            raise
        except:
            print('no exception ocurred')
            currenttime = moment.now().strftime("%H-%M-%S_%d%m_%Y")
            testname = utils.whoami()
            screenshot = testname + "_" + currenttime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot,
                          attachment_type=allure.attachment_type.PNG)
            raise

        finally:
            print('i will execute anyway')



