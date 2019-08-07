# coding=utf-8
from organization.views import OrgView,AddUserAskView

__author__ = 'chen'
__date__ = '2019/8/7 21:38'

from django.conf.urls import url, include

urlpatterns = [
    # 课程机构列表页
    url(r'^org_list/$', OrgView.as_view(), name='org_list'),
    url(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask'),
]
