from selenium.webdriver.common.by import By


class Log_in_out:
    def __init__(self,driver):
        self.username = By.ID,'account'
        self.password = By.NAME,'password'
        self.login = By.ID,'submit'
        self.myframe = 'appIframe-my'
        self.usermenu = By.ID,'userMenu'
        self.out = By.CSS_SELECTOR,'a[target = _top]'
        self.browser = driver

    def clear_username(self):
        self.browser.find_element(*self.username).clear()

    def clear_password(self):
        self.browser.find_element(*self.password).clear()

    def input_username(self,username):
        self.browser.find_element(*self.username).send_keys(username)

    def input_password(self,password):
        self.browser.find_element(*self.password).send_keys(password)

    def click_login(self):
        self.browser.find_element(*self.login).click()

    def click_userMenu(self):
        self.browser.find_element(*self.usermenu).click()

    def click_out(self):
        self.browser.find_element(*self.out).click()

class UserAdd:
    def __init__(self,driver):
        self.backstage = By.CSS_SELECTOR,'[data-app = admin]'
        self.bsframe = 'appIframe-admin'
        self.users = By.LINK_TEXT, '人员'
        self.addu = By.CSS_SELECTOR, 'a[href$= "user-create-0.html"]'
        self.uname = By.ID, 'account'
        self.upw1 = By.ID, 'password1'
        self.upw2 = By.ID, 'password2'
        self.rname = By.ID, 'realname'
        self.email = By.ID, 'email'
        self.role = By.ID, 'role'
        self.commiter = By.XPATH, '//input[@id = "commiter"]'
        self.syspw = By.CSS_SELECTOR, 'input[id^= "verify"]'
        self.save = By.ID,'submit'
        self.browser = driver

    def click_backstage(self):
        self.browser.find_element(*self.backstage).click()

    def click_users(self):
        self.browser.find_element(*self.users).click()

    def click_addu(self):
        self.browser.find_element(*self.addu).click()

    def input_username(self,uname):
        self.browser.find_element(*self.uname).send_keys(uname)

    def input_password1(self, password):
        self.browser.find_element(*self.upw1).send_keys(password)

    def input_password2(self, password):
        self.browser.find_element(*self.upw2).send_keys(password)

    def input_realname(self,rname):
        self.browser.find_element(*self.rname).send_keys(rname)

    def input_email(self,email):
        self.browser.find_element(*self.email).send_keys(email)

    def select_role(self):
        return self.browser.find_element(*self.role)

    def input_commiter(self,commiter):
        self.browser.find_element(*self.commiter).send_keys(commiter)

    def input_syspassword(self,syspw):
        self.browser.find_element(*self.syspw).send_keys(syspw)

    def click_save(self):
        self.browser.find_element(*self.save).click()

# class BugSubmit:
#     def __init__(self, driver):
#         self.test = By.CSS_SELECTOR, 'li[title = 测试]'
#         self.testframe = 'appIframe-qa'
#         self.bug = By.LINK_TEXT, 'Bug'
#         self.sub_nbug = By.XPATH,'//div//a[@href = "/zentao/bug-create-1-0-moduleID=0.html"]'
#         self.module_sel = By.CSS_SELECTOR,'a[class = chosen-single]'
#         self.module = By.CSS_SELECTOR, 'li[title = "/登录"][data-option-array-index = "1"]'
#         self.project_sel = By.CLASS_NAME, 'chosen-default'
#         self.project = By.CSS_SELECTOR, 'li[title = "禅道2.0"]'
#         self.version_sel = By.CLASS_NAME, 'chosen-choices'
#         self.version = By.CSS_SELECTOR, 'li[title = 主干]'
#         self.loadalluser = By.CSS_SELECTOR, 'button[onclick = "loadAllUsers()"]'
#         self.assign = By.CLASS_NAME, 'chosen-default'
#         self.assignuser = By.CSS_SELECTOR, 'li[title = "A:张三"]'
#         self.dateline = By.ID, 'deadline'
#         self.os_sel = By.CLASS_NAME, 'chosen-default'
#         self.os = By.CSS_SELECTOR, 'li[title = "Windows 10"]'
#         self.browser_sel = By.CLASS_NAME, 'chosen-default'
#         self.browser_ = By.CSS_SELECTOR, 'li[title = chrome]'
#         self.bugtitle = By.ID, 'title'
#         self.btseverity = By.CSS_SELECTOR, 'div[data-type = severity]'
#         self.severity = By.XPATH, '//div//div//select[@id = "severity"]'
#         self.btpriority = By.CSS_SELECTOR, 'div[data-type = pri]'
#         self.priority = By.ID, 'pri'
#         self.editframe = By.CLASS_NAME, 'ke-edit-iframe'
#         self.body = By.CLASS_NAME, 'article-content'
#         self.bugsub = By.ID, 'submit'
#         self.browser = driver
#
#     def click_test(self):
#         self.browser.find_element(*self.test).click()
#
#     def click_bug(self):
#         self.browser.find_element(*self.bug).click()
#
#     def click_sub_nbug(self):
#         self.browser.find_element(*self.sub_nbug).click()
#
#     def click_module_sel(self):
#         self.browser.find_elements(*self.module_sel)[1].click()
#
#     def click_module(self):
#         self.browser.find_element(*self.module).click()
#
#     def click_project_sel(self):
#         self.browser.find_elements(*self.project_sel)[0].click()
#
#     def click_project(self):
#         self.browser.find_element(*self.project).click()
#
#     def click_version_sel(self):
#         self.browser.find_element(*self.version_sel).click()
#
#     def click_version(self):
#         self.browser.find_element(*self.version).click()
#
#     def click_loadalluser(self):
#         self.browser.find_element(*self.loadalluser).click()
#
#     def click_assign(self):
#         self.browser.find_elements(*self.assign)[1].click()
#
#     def click_assignuser(self):
#         self.browser.find_element(*self.assignuser).click()
#
#     def input_dateline(self,dateline):
#         self.browser.find_element(*self.dateline).send_keys(dateline)
#
#     def click_os_sel(self):
#         self.browser.find_elements(*self.os_sel)[1].click()
#
#     def click_os(self):
#         self.browser.find_element(*self.os).click()
#
#     def click_browser_sel(self):
#         self.browser.find_elements(*self.browser_sel)[1].click()
#
#     def click_browser_(self):
#         self.browser.find_element(*self.browser_).click()
#
#     def input_bugtitle(self, bugtitle):
#         self.browser.find_element(*self.bugtitle).send_keys(bugtitle)
#
#     def click_btseverity(self):
#         self.browser.find_element(*self.btseverity).click()
#
#     def select_severity(self):
#         return self.browser.find_element(*self.severity)
#
#     def click_btpriority(self):
#         self.browser.find_element(*self.btpriority).click()
#
#     def select_priority(self):
#         return self.browser.find_element(*self.priority)
#
#     def to_editframe(self):
#         return self.browser.find_element(*self.editframe)
#
#     def clear_text(self):
#         self.browser.find_element(*self.body).clear()
#
#     def input_step(self,step):
#         self.browser.find_element(*self.body).send_keys(step)
#
#     def input_result(self,result):
#         self.browser.find_element(*self.body).send_keys(result)
#
#     def input_expect(self,expect):
#         self.browser.find_element(*self.body).send_keys(expect)
#
#     def click_bugsub(self):
#         self.browser.find_element(*self.bugsub).click()

