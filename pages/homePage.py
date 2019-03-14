class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.welcome_id ='welcome'
        self.logout_link = 'Logout'

    def click_on_welcomedrpdwn(self):
        self.driver.find_element_by_id(self.welcome_id).click()

    def click_on_logout_button(self):
        self.driver.find_element_by_link_text(self.logout_link)