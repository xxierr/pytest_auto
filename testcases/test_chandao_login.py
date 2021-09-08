from config.config import file
from pageobjects.test_chandao import Log_in_out
from data.testdata import RWxlsx
import pytest
import time


class TestChandao():
    F = RWxlsx(file, 1)
    Fv = F.read()
    test1 = Fv[0]
    test2 = Fv[1]

    @pytest.mark.parametrize('test1', [test1])
    # @pytest.mark.smoke
    @pytest.mark.run(order=2)
    # @pytest.mark.flaky(reruns=1)
    def test_login1(self, test1, test_inout):
        name = test1[0]
        pw = test1[1]
        page = Log_in_out(test_inout)
        if page.browser.title == '欢迎使用禅道集成运行环境！':
            page.browser.find_element_by_id("zentao").click()
        elif page.browser.title == '用户登录 - 禅道':
            page.clear_username()
            page.clear_password()
            page.input_username(name)
            time.sleep(4)
            page.input_password(pw)
            time.sleep(3)
            # a = 1
            # assert a == 2
            try:
                page.click_login()
                time.sleep(5)
                assert page.browser.title == '地盘 - 禅道'
                print("登录成功")
            except AssertionError:
                print("登录失败")

    @pytest.mark.parametrize('test2', [test2])
    @pytest.mark.run(order=1)
    # @pytest.mark.skip
    def test_login2(self,test2,test_inout):
        name = test2[0]
        pw = test2[1]
        page = Log_in_out(test_inout)
        if page.browser.title == '欢迎使用禅道集成运行环境！':
            page.browser.find_element_by_id("zentao").click()
        elif page.browser.title == '用户登录 - 禅道':
            page.clear_username()
            page.clear_password()
            page.input_username(name)
            time.sleep(4)
            page.input_password(pw)
            try:
                page.click_login()
                time.sleep(3)
                alert = page.browser.switch_to.alert
                content = alert.text
                alert.accept()
                assert '登录失败' in content or '尝试机会' in content
                print('测试用例执行成功，验证错误的密码')
            except AssertionError:
                print('测试用例执行失败')


# if __name__ == '__main__':
#     pytest.main(['-vs', 'test_chandao6.py'])
if __name__ == '__main__':
    pytest.main(['-s', 'test_chandao6.py'])
