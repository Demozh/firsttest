#-*-coding:utf-8-*- 
#
#python学习交流群：516107834
import hashlib
import json
from datetime import *
from urllib import parse
from io import BytesIO
import config

import requests
from PIL import Image

# 禁用安全请求警告
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning

disable_warnings(InsecureRequestWarning)

# 账户名 密码
USERNAME = '15638538130'
PASSWORD = 'ztx156763'

# 若快打码 地址 [url=http://www.ruokuai.com]http://www.ruokuai.com[/url]
RUOUSER = 'chendada123'
RUOPASS = 'aa123456'

session = requests.session()
session.verify = False

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Host": "kyfw.12306.cn",
    "Referer": "https://kyfw.12306.cn/otn/passport?redirect=/otn/"
}
imgPath = 'code.png'


def login():
    # 打开登录页面
    url = "https://kyfw.12306.cn/otn/login/init"
    session.get(url, headers=headers)
    # 发送验证码
    if not captcha():
        return False

    # 发送登录信息
    data = {
        "username": USERNAME,
        "password": PASSWORD,
        "appid": "otn"
    }
    url = "https://kyfw.12306.cn/passport/web/login"
    response = session.post(url, headers=headers, data=data)
    if response.status_code == 200:
        result = json.loads(response.text)
        print(result.get("result_message"), result.get("result_code"))
        if result.get("result_code") != 0:
            return False

    data = {
        "appid": "otn"
    }
    url = "https://kyfw.12306.cn/passport/web/auth/uamtk"
    response = session.post(url, headers=headers, data=data)
    if response.status_code == 200:
        result = json.loads(response.text)
        print(result.get("result_message"))
        newapptk = result.get("newapptk")

    data = {
        "tk": newapptk
    }
    url = "https://kyfw.12306.cn/otn/uamauthclient"
    response = session.post(url, headers=headers, data=data)
    if response.status_code == 200:
        print(response.text)

    url = "https://kyfw.12306.cn/otn/index/initMy12306"
    response = session.get(url, headers=headers)
    if response.status_code == 200 and response.text.find("用户名") != -1:
        return True
    return False


def captcha():
    data = {
        "login_site": "E",
        "module": "login",
        "rand": "sjrand",
        "0.17231872703389062": ""
    }

    # 获取验证码
    param = parse.urlencode(data)
    url = "https://kyfw.12306.cn/passport/captcha/captcha-image?{}".format(param)
    response = session.get(url, headers=headers)
    if response.status_code == 200:
        file = BytesIO(response.content)
        img = Image.open(file)
        img.save(imgPath, format="png")
        img.show()

    codeStr = getCode(imgPath)
    print(codeStr)
    a = ''
    b = ''
    c = ''
    d = ''
    e = ''
    f = ''
    g = ''
    h = ''
    if '1' in codeStr:
        a = '37,37,'
    if '2' in codeStr:
        b = '100,37,'
    if '3' in codeStr:
        c = '180,37,'
    if '4' in codeStr:
        d = '250,37,'
    if '5' in codeStr:
        e = '37,100,'
    if '6' in codeStr:
        f = '100,100,'
    if '7' in codeStr:
        g = '180,100,'
    if '8' in codeStr:
        h = '250,100,'

    newCodeStr = a + b + c + d + e + f + g + h
    newStr = newCodeStr[:-1]
    # 发送验证码
    data = {
        "answer": newStr,
        "login_site": "E",
        "rand": "sjrand"
    }

    url = "https://kyfw.12306.cn/passport/captcha/captcha-check"
    response = session.post(url, headers=headers, data=data)
    if response.status_code == 200:
        result = json.loads(response.text)
        print(result.get("result_message"))
        return True if result.get("result_code") == "4" else False
    return False


# 获取联系人
def getUser():
    url = 'https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs'
    response = session.get(url, headers=headers)
    result = json.loads(response.text)
    data = result['data']['normal_passengers']
    if (data):
        print(data)
    # print(response.text)


# 若快 12306打码 直接传入本地文件路径
def getCode(img):
    url = "http://api.ruokuai.com/create.json"
    fileBytes = open(img, "rb").read()
    paramDict = {
        'username': RUOUSER,
        'password': RUOPASS,
        'typeid': 6113,
        'timeout': 90,
        'softid': 115039,
        'softkey': 'ea747bbf5e734e79bc9cb3b68f7fbe54'
    }
    paramKeys = ['username',
                 'password',
                 'typeid',
                 'timeout',
                 'softid',
                 'softkey'
                 ]
    result = http_upload_image(url, paramKeys, paramDict, fileBytes)
    return result['Result']


# 若快12306打码 上传图片
def http_upload_image(url, paramKeys, paramDict, filebytes):
    timestr = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    boundary = '------------' + hashlib.md5(timestr.encode("utf8")).hexdigest().lower()
    boundarystr = '\r\n--%s\r\n' % (boundary)

    bs = b''
    for key in paramKeys:
        bs = bs + boundarystr.encode('ascii')
        param = "Content-Disposition: form-data; name=\"%s\"\r\n\r\n%s" % (key, paramDict[key])
        # print param
        bs = bs + param.encode('utf8')
    bs = bs + boundarystr.encode('ascii')

    header = 'Content-Disposition: form-data; name=\"image\"; filename=\"%s\"\r\nContent-Type: image/gif\r\n\r\n' % (
        'sample')
    bs = bs + header.encode('utf8')

    bs = bs + filebytes
    tailer = '\r\n--%s--\r\n' % (boundary)
    bs = bs + tailer.encode('ascii')

    import requests
    headers = {'Content-Type': 'multipart/form-data; boundary=%s' % boundary,
               'Connection': 'Keep-Alive',
               'Expect': '100-continue',
               }
    response = requests.post(url, params='', data=bs, headers=headers)
    return response.json()


if __name__ == "__main__":

    # 登陆
    if login():
        print("Success")
    else:
        print("Failed")
    # 获取用户联系人信息
    getUser()
