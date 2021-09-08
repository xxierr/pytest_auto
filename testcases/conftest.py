import pytest
import time
from appium import webdriver
from config.config import driver_path, caps, path, url
from common.function import init_isexec
import selenium.webdriver
from pageobjects.test_chandao import Log_in_out


@pytest.fixture(scope='session')
def test_inout():
    browser = selenium.webdriver.Chrome(executable_path=path)
    browser.maximize_window()
    browser.get(url)
    browser.implicitly_wait(10)  #隐形等待
    assert browser.title == '欢迎使用禅道集成运行环境！' or '用户登录 - 禅道'
    print('成功打开浏览器并进入禅道')
    yield browser
    time.sleep(2)
    if browser.title == '地盘 - 禅道':
        page = Log_in_out(browser)
        browser.switch_to.frame(page.myframe)
        page.click_userMenu()
        time.sleep(2)
        page.click_out()
    assert browser.title == '用户登录 - 禅道'
    print('退出成功！')
    time.sleep(5)
    browser.quit()
    print('成功关闭浏览器！')


@pytest.fixture(scope='session')
def test_init():
    init_isexec()


@pytest.fixture(scope='session')
def test_open():
    app_driver = webdriver.Remote(driver_path, caps)
    app_driver.implicitly_wait(30)
    time.sleep(3)
    activity = app_driver.current_activity.title()
    assert activity == 'Com.Tencent.Mobileqq.Activity.Splashactivity' or activity == \
        'Com.Tencent.Mobileqq.Activity.Loginactivity' or activity == \
        'Com.Tencent.Mobileqq.Activity.Registerguideactivity'
    print('成功打开QQ')
    yield app_driver
    time.sleep(10)
    app_driver.quit()
    print('成功关闭QQ！')
