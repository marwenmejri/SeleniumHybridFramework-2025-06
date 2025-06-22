from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        
    def set_username(self, username):
        self.driver.find_element(by=By.ID,value='username').send_keys(username)

    def set_password(self, password):
        self.driver.find_element(by=By.ID, value='password').send_keys(password)

    def login(self):
        self.driver.find_element(by=By.ID,value='submit').click()

    def logout(self):
        self.driver.find_element(by=By.XPATH, value='//a[normalize-space()="Log out"]').click()


# if __name__ == '__main__':
#     # Initialize the Chrome driver
#     driver1 = Chrome()
#     driver1.maximize_window()
#     driver1.implicitly_wait(time_to_wait=10)
#     driver1.get(url='https://practicetestautomation.com/practice-test-login/')

#     # Create an instance of LoginPage
#     lp = LoginPage(driver=driver1)
#     time.sleep(2)
#     lp.set_username(username='student')
#     time.sleep(2)
#     lp.set_password(password='Password123')
#     time.sleep(2)
#     lp.login()
#     time.sleep(2)
#     if driver1.title == 'Logged In Successfully | Practice Test Automation':
#         print(f'Login successful for user: student')
#         lp.logout()
#         time.sleep(2)
#     driver1.quit()