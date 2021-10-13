class loginpage():
    def __init__(self,driver):
        driver = self.driver
        self.txt_username_id = "txtUsername"
        self.txt_password_id = "txtPassword"
        self.txt_login_button_id = "btnLogin"

    def enter_username(self,username):
        self.driver.find_element_by_id(self.txt_username_id).clear()
        self.driver.find_element_by_id(self.txt_username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.txt_password_id).clear()
        self.driver.find_element_by_id(self.txt_password_id).send_keys(password)
    def click_login(self):
        self.driver.find_element_by_id(self.txt_login_button_id).click()