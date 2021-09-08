from common.function import get_params, result_status, send_request
from log.log import logger
import pytest


class Test_homepage:
    caseid = ['Newb_001']

    @pytest.mark.parametrize('case_id', caseid)
    def test_firstpage(self,case_id,test_init):
        data = get_params(case_id)
        reps = send_request(data)
        expectvalue = data[4]
        try:
            assert expectvalue in reps
            print("测试成功")
            result_status(case_id, 'Passed')
        except AssertionError:
            print("测试失败")
            result_status(case_id, 'Failed')
        logger.info('验证获取首页信息成功的用例！')
