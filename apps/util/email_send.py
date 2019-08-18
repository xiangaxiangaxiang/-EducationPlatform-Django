# coding=utf-8
__author__ = 'chen'
__date__ = '2019/8/3 11:52'
from random import Random

from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from DjangoEducationPlatform.settings import EMAIL_FROM


# 获取随机验证码
def random_str(randomlength=8):
    code = ''
    chars = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789'
    length = len(chars)
    random = Random()
    for i in range(randomlength):
        code = chars[random.randint(0, length)]
    return code


# 发送注册邮件
def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    if send_type == 'update_email':
        code = random_str(4)
    else:
        code = random_str(16)
    email_record.email = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()
    email_title = ''
    email_body = ''
    if send_type == 'register':
        email_title = '德玛西亚学院注册激活链接'
        email_body = '请点击下面链接激活你的账号： http://127.0.0.1:8000/active/{0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == 'forget':
        email_title = '德玛西亚学院密码重置链接'
        email_body = '请点击下面链接重置你的密码： http://127.0.0.1:8000/reset/{0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == 'update_email':
        email_title = '德玛西亚学院修改邮箱验证码'
        email_body = '你的邮箱验证码为： {0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass