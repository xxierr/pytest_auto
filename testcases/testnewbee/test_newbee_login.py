from common.function import get_params, result_status, send_request, write_token
from config.config import idnum
from log.log import logger
import pytest


class Test_login:
    caseid = ['Newb_002']

    @pytest.mark.parametrize('case_id', caseid)
    def test_login(self,case_id,test_init):
        data = get_params(case_id)
        reps = send_request(data)
        repse = eval(reps)
        token = repse.get('data')
        expectvalue = data[4]
        try:
            assert expectvalue in reps
            print("测试成功")
            result_status(case_id, 'Passed')
            write_token(token, idnum)
        except AssertionError:
            print("测试失败")
            result_status(case_id, 'Failed')
        logger.info('验证用户登录成功的用例！')
