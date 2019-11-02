import requests
import random
def open():

    url = "http://106.ihuyi.com/webservice/sms.php?method=Submit" #接口地址，文档当中有用
    a = random.randrange(1, 1000000)
    #APIID
    account = "C53177860" #官方的校验
    #APIkey
    password = "6f7877f95c757ef36a09d51c49e653e7" #官方的校验

    mobile = "13331153360"  #接受人 #13331153360
    content = "您的验证码是：{:0>6}。请不要把验证码泄露给其他人。".format(a) #发送内容，格式固定

    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        "Accept": "text/plain"
    } #请求的格式

    data = {
        "account": account,
        "password": password,
        "mobile": mobile,
        "content": content,
    } #要发送的数据
    response = requests.post(url,headers = headers,data=data) #发起请求
    print(response.content.decode()) #返回结构
# import smtplib
# from email.mime.text import MIMEText
#
# content = """
#     <a href='www.baidu.com'>点击</a>
# """
#
# sender = '1339566602@qq.com'
# receiver = """
# 645206281@qq.com,
# 876911388@qq.com,
# 1339566602@qq.com"""
# password = 'kdvcykwjzpfmhddj'
# message = MIMEText(content,'html','utf-8')
# message['To'] = receiver
# message['From'] = sender
# message['Subject'] = '疯狂点击'
#
# smtp = smtplib.SMTP_SSL('smtp.qq.com',465)
# smtp.login(sender,password)
# smtp.sendmail(sender,receiver.split(',\n'),message.as_string())
