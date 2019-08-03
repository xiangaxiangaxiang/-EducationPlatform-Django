# coding=utf-8
__author__ = 'chen'
__date__ = '2019/8/2 21:33'
from django import forms
from captcha.fields import CaptchaField


class LoginForm():
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm():
    email = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={'invalid': u'验证码错误'})


class ForgetForm():
    email = forms.CharField(required=True)
    captcha = CaptchaField(error_messages={'invalid': u'验证码错误'})


class ModifyPwdForm():
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)
