# coding=utf-8
__author__ = 'chen'
__date__ = '2019/7/28 10:54'

import xadmin
from xadmin import views
from models import Course, CourseResource, Video, Lesson


# 允许修改主题
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


# 全局属性，设置左上角的title，最底部的声明和左侧导航栏的样式
class GlobalSettings(object):
    site_title = '教育平台后台管理系统'
    site_footer = '德玛西亚学院'
    menu_style = 'accordion'


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'students', 'learn_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']
    list_filter = ['name', 'desc', 'detail', 'degree', 'students', 'learn_time']


class LessonAdmin(object):

    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)