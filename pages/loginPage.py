class LoginPage():
    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = 'txtUsername'
        self.password_textbox_id ='txtPassword'
        self.loginButton_id = 'btnLogin'

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)



    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys('admin123')

    def click_onLogin_button(self):
        self.driver.find_element_by_id('btnLogin').click()