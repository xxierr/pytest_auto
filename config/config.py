import os

url = "http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html"
driver_path = r"http://localhost:4723/wd/hub"
idnum = 4
caps = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "HUAWEI MLA-AL10",
    "appPackage": "com.tencent.qqlite",
    "appActivity": "com.tencent.mobileqq.activity.SplashActivity",
    "noReset": True
}
project_file = os.path.dirname(os.path.dirname(__file__))
logfile = project_file + r"/log/log.txt"
datafile_p = project_file + r"/data/apidata.xlsx"
file = project_file + r"\data\webtestdata.xlsx"
path = project_file + r"\driver\chromedriver.exe"
file_path = project_file + r"\data\testdata.xlsx"
report_path = project_file + r"\result"
case_path = project_file + r"\testcases"
img_path = project_file + r"\result\error_img"
