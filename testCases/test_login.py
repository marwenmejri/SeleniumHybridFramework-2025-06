from selenium.webdriver import Chrome
import time

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import get_password, get_username, get_url
from utilities.customLogger import create_logger


logger = create_logger(filename='Logs/logs.log',
                       filemode='a')


class Test001Login:
    baseURL = get_url()
    username = get_username()
    password = get_password()

    def test_verify_login_page_title(self, setup):
        logger.info("************ Test001Login ************")
        logger.info("************ test_verify_login_page_title STARTED ************")
        driver = setup
        driver.get(url=self.baseURL)
        time.sleep(2)
        expected_title = "Test Login | Practice Test Automation"
        if driver.title == expected_title:
            logger.info("************ test_verify_login_page_title PASSED ************")
            # driver.quit()
            assert True
        else:
            # driver.quit()
            driver.save_screenshot(filename="Screenshots/test_verify_login_page_title_failed.png")
            logger.error("************ test_verify_login_page_title FAILED ************")
            assert False

    def test_login_positive(self, setup):
        logger.info("************ test_login_positive STARTED ************")
        driver = setup
        driver.get(url=self.baseURL)
        time.sleep(2)

        lp = LoginPage(driver=driver)
        lp.set_username(username=self.username)
        time.sleep(2)
        lp.set_password(password=self.password)
        time.sleep(2)
        lp.login()
        time.sleep(2)

        new_page_url = driver.current_url
        expected_string_url = "practicetestautomation.com/logged-in-successfully/"
        if expected_string_url in new_page_url:
            lp.logout()
            time.sleep(2)
            logger.info("************ test_login_positive PASSED ************")
            # driver.quit()
            assert True
        else:
            time.sleep(2)
            driver.save_screenshot(filename="Screenshots/test_login_positive_failed.png")
            logger.error("************ test_login_positive FAILED ************")
            # driver.quit()
            assert False

    def test_negative_username(self, setup):
        logger.info("************ test_negative_username STARTED ************")
        driver = setup
        driver.get(url=self.baseURL)
        time.sleep(2)

        lp = LoginPage(driver=driver)
        lp.set_username(username="incorrectUser")
        time.sleep(2)
        lp.set_password(password=self.password)
        time.sleep(2)
        lp.login()
        time.sleep(2)

        if "Your username is invalid!" in driver.page_source:
            logger.info("************ test_negative_username PASSED ************")
            # driver.quit()
            assert True
        else:
            # driver.quit()
            driver.save_screenshot(filename="Screenshots/test_negative_username_fail.png")
            logger.error("************ test_negative_username FAILED ************")
            assert False


class Test002Login:
    baseURL = get_url()
    username = get_username()
    password = get_password()

    def test_verify_login_page_title2(self, setup):
        logger.info("************ Test002Login ************")
        logger.info("************ test_verify_login_page_title2 STARTED ************")
        driver = setup
        driver.get(url=self.baseURL)
        time.sleep(2)
        expected_title = "Test Login | Practice Test Automation"
        if driver.title == expected_title:
            logger.info("************ test_verify_login_page_title2 PASSED ************")
            # driver.quit()
            assert True
        else:
            # driver.quit()
            driver.save_screenshot(filename="Screenshots/test_verify_login_page_title_failed2.png")
            logger.error("************ test_verify_login_page_title2 FAILED ************")
            assert False

    def test_login_positive2(self, setup):
        logger.info("************ test_login_positive2 STARTED ************")
        driver = setup
        driver.get(url=self.baseURL)
        time.sleep(2)

        lp = LoginPage(driver=driver)
        lp.set_username(username=self.username)
        time.sleep(2)
        lp.set_password(password=self.password)
        time.sleep(2)
        lp.login()
        time.sleep(2)

        new_page_url = driver.current_url
        expected_string_url = "practicetestautomation.com/logged-in-successfully/"
        if expected_string_url in new_page_url:
            lp.logout()
            time.sleep(2)
            logger.info("************ test_login_positive2 PASSED ************")
            # driver.quit()
            assert True
        else:
            time.sleep(2)
            driver.save_screenshot(filename="Screenshots/test_login_positive_failed2.png")
            logger.error("************ test_login_positive2 FAILED ************")
            # driver.quit()
            assert False

    def test_negative_username2(self, setup):
        logger.info("************ test_negative_username2 STARTED ************")
        driver = setup
        driver.get(url=self.baseURL)
        time.sleep(2)

        lp = LoginPage(driver=driver)
        lp.set_username(username="incorrectUser")
        time.sleep(2)
        lp.set_password(password=self.password)
        time.sleep(2)
        lp.login()
        time.sleep(2)

        if "Your username is invalid!" in driver.page_source:
            logger.info("************ test_negative_username2 PASSED ************")
            # driver.quit()
            assert True
        else:
            # driver.quit()
            driver.save_screenshot(filename="Screenshots/test_negative_username_fail2.png")
            logger.error("************ test_negative_username2 FAILED ************")
            assert False

