# coding=utf-8
__author__ = 'chen'
__date__ = '2019/8/2 21:33'
from django import forms


class LoginForm():
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
