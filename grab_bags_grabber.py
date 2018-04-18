from twilio.rest import Client
from urllib import request
from bs4 import BeautifulSoup
import json
import time

account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

def sendmessage(code):
    to_ = ""
    from_ = ""
    if code == 1:
        message = client.messages.create(
            to_,
            body = "垃圾包上线了!",
            from_= from_
        )
    else:
        message = client.messages.creat(
            to_,
            body = "运行出问题了",
            from_= from_
        )

def checkstatus():
    status = 0
    with request.urlopen("https://pimpmykeyboard.com/grab-bags/", timeout=30) as f:
        data = f.read()
        data = str(data)
        if '"instock":true' in data:
            status = 1
            print("有货")
            sendmessage(status)
            return 0
        elif '"instock":false' in data:
            print("缺货")
            return 1
        # print('Status:', f.status, f.reason)
        # print('Data:', data.decode('utf-8'))
        # pmk = BeautifulSoup(data, 'lxml')
        # print(pmk)
        # pmk = pmk.find_all('script')
        # for script in pmk:
        #     if 'language' in script.attrs.keys():
        #         print(script)
        #         if '"instock":false' in script.string:
        #             print('ok')
        #         break

while 1 == 1:
    num = 0
    try:
        if checkstatus() == 0:
            break
        time.sleep(60)
    except:
        num += 1
        print("出问题了")
        if num % 6 ==0:
            sendmessage(num)
        continue
