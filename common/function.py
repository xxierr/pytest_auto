import requests
from data.read_write import ReadWrite


def get_params(caseid):
    excels = ReadWrite(1)
    payload = excels.read()
    flag = 0
    for i in range(len(payload)):
        if payload[i].get(ReadWrite.caseid) == caseid:
            url = payload[i].get(ReadWrite.requestaddress)
            method = payload[i].get(ReadWrite.requestmethod)
            data = payload[i].get(ReadWrite.requestparam)
            header = payload[i].get(ReadWrite.requestheader)
            expect = payload[i].get(ReadWrite.expectresult)
            flag = 1
            break
    if flag == 0:
        print("测试用例不存在")
    return url, method, data, header, expect


def send_request(values):
    global resp_content
    url = values[0]
    method = values[1]
    data = values[2]
    header = eval((values[3]))
    if method == 'get' or method == 'Get' or method == 'GET':
        req = requests.get(url=url, headers=header)
        resp_content = req.text
    elif method == 'post' or method == 'Post' or method == "POST":
        req = requests.post(url=url, data=data, headers=header)
        resp_content = req.text
    return resp_content


def result_status(caseid, actual):
    excels = ReadWrite(1)
    excels.write(caseid, actual)


def write_token(token, idnum):
    excels = ReadWrite(1)
    excels.writetoken(token, idnum)


def init_isexec():
    excels = ReadWrite(1)
    excels.initexec()
