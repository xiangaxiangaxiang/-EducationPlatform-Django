# coding=utf-8
__author__ = 'chen'
__date__ = '2019/8/12 21:44'
from django.conf.urls import url, include
from courses.views import CourseListView,CourseDetailView,CourseInfoView,CourseCommentsView,AddCommentsView

urlpatterns = [
    # 课程机构列表页
    url(r'^list/$', CourseListView.as_view(), name='course_list'),
    # 课程详情
    url(r'detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='course_detail'),

    url(r'info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name='course_info'),
    # 课程评论
    url(r'comment/(?P<course_id>\d+)/$', CourseCommentsView.as_view(), name='course_comments'),
    # 课程评论
    url(r'^add_comment/$', AddCommentsView.as_view(), name='add_comment'),
]
