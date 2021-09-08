from BeautifulReport import BeautifulReport
from config.config import file_path
from data.testdata import RWxlsx
from pageobjects.test_qq import Login
from log.log import logger
from common.comm import save_img
import time
import pytest


class Test_qq():
    F = RWxlsx(file_path, 1)
    Fv = F.read()
    test1 = Fv[0]
    usernum = test1[0]
    pw = test1[1]

    @BeautifulReport.add_test_img("test_login图片")
    @pytest.mark.parametrize('test1', [test1])
    def test_login(self,test1,test_open):
        usernum = test1[0]
        pw = test1[1]
        page = Login(test_open)
        if page.appdriver.current_activity.title() == 'Com.Tencent.Mobileqq.Activity.Registerguideactivity':
            time.sleep(6)
            page.click_loginmodule()
        if page.appdriver.current_activity.title() == 'Com.Tencent.Mobileqq.Activity.Loginactivity':
            page.appdriver.implicitly_wait(20)
            time.sleep(5)
            page.input_usernumber(usernum)
            time.sleep(2)
            page.input_password(pw)
            try:
                page.click_login()
                time.sleep(20)
                act = page.appdriver.current_activity.title()
                assert act == 'Com.Tencent.Mobileqq.Activity.Splashactivity'
                print('登录成功')
            except:
                print('登录失败')
                save_img(page.appdriver, 'test_login图片')
        logger.info('验证QQ成功登录的用例')


if __name__ == '__main__':
    pytest.main(['-s', 'test_loginqq.py'])
