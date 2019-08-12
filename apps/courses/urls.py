# coding=utf-8
__author__ = 'chen'
__date__ = '2019/8/12 21:44'
from django.conf.urls import url, include
from courses.views import CourseListView,CourseDetailView

urlpatterns = [
    # 课程机构列表页
    url(r'^list/$', CourseListView.as_view(), name='course_list'),
    # 课程详情
    url(r'detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='course_detail'),
]
