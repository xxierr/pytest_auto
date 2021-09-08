

class Login:
    def __init__(self,driver):
        self.usernumber = '请输入QQ号码或手机或邮箱'
        self.password = 'com.tencent.qqlite:id/password'
        self.login = 'com.tencent.qqlite:id/login'
        self.loginmodule = 'text("登录")'
        self.appdriver = driver

    def input_usernumber(self,usernumber):
        self.appdriver.find_element_by_accessibility_id(self.usernumber).send_keys(usernumber)

    def input_password(self,password):
        self.appdriver.find_element_by_id(self.password).send_keys(password)

    def click_login(self):
        self.appdriver.find_element_by_id(self.login).click()

    def click_loginmodule(self):
        self.appdriver.find_element_by_android_uiautomator(self.loginmodule).click()
