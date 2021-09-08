import pytest
import subprocess

which = input("请输入相应单词要执行哪种测试('app'.'api'.'web'之中选一，或输入'all'执行所有测试)：")
if which == 'app':
    pytest.main(['-s', './testcases/test_loginqq.py'])
elif which == 'api':
    pytest.main(['-s', './testcases/testnewbee/'])
elif which == 'web':
    pytest.main(['-s', './testcases/test_chandao_login.py'])
elif which == 'all':
    pytest.main()
else:
    print('输入错误！请退出重新输入选择')
subprocess.call('allure generate ./result/temp -o ./result/report --clean', shell=True)  # -o是输出
subprocess.call('allure open -h 127.0.0.1 ./result/report', shell=True)
