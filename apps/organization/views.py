# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from models import CourseOrg, CityDict
from operation.models import UserFavorite
# Create your views here.
from organization.forms import UserAskForm


class OrgView(View):
    def get(self, request):
        # 课程机构
        all_orgs = CourseOrg.objects.all()
        hot_orgs = all_orgs.order_by('click_nums')[:3]
        # 城市
        all_city = CityDict.objects.all()
        # 取出筛选城市
        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        # 类别筛选
        category = request.GET.get('ct', '')
        if category:
            all_orgs = all_orgs.filter(category=category)

        # 排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                all_orgs = all_orgs.order_by('-students')
            elif sort == 'courses':
                all_orgs = all_orgs.order_by('-course_nums')

        # 对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs, 5, request=request)
        orgs = p.page(page)

        org_nums = all_orgs.count()
        return render(request, 'org-list.html', {
            'all_org': orgs,
            'all_city': all_city,
            'org_nums': org_nums,
            'city_id': city_id,
            'category': category,
            'hot_orgs': hot_orgs,
            'sort': sort
        })


class AddUserAskView(View):
    # 用户添加查询
    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.valid():
            user_ask = userask_form.save(commit=True)
            return HttpResponse("{'status': 'success'}", content_type='application/json')
        else:
            return HttpResponse("{'status': 'fail', 'msg': {0}}".format(userask_form.errors), content_type='application/json')


class OrgHomeView(View):
    # 机构首页
    def get(self, request, org_id):
        current_page = 'home'
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request, fav_id=course_org.id, fav_type=2):
                has_fav = True
        all_course = course_org.course_set.all()[:3]
        all_teacher = course_org.course_set.all()[:3]
        return render(request, 'org-detail-homepage.html', {
            'all_course': all_course,
            'all_teacher': all_teacher,
            'course_org': course_org,
            'current_page': current_page,
            'has_fav': has_fav
        })

class OrgCourseView(View):
    # 机构课程列表页
    def get(self, request, org_id):
        current_page = 'course'
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request, fav_id=course_org.id, fav_type=2):
                has_fav = True
        all_course = course_org.course_set.all()
        return render(request, 'org-detail-course.html', {
            'all_course': all_course,
            'course_org': course_org,
            'current_page': current_page,
            'has_fav': has_fav
        })


class OrgDescView(View):
    # 机构课程介绍页
    def get(self, request, org_id):
        current_page = 'desc'
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request, fav_id=course_org.id, fav_type=2):
                has_fav = True
        return render(request, 'org-detail-desc.html', {
            'current_page': current_page,
            'course_org': course_org,
            'has_fav': has_fav
        })


class OrgTeacherView(View):
    # 机构教师页
    def get(self, request, org_id):
        current_page = 'desc'
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_teacher = course_org.teacher_set.all()
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request, fav_id=course_org.id, fav_type=2):
                has_fav = True
        return render(request, 'org-detail-desc.html', {
            'current_page': current_page,
            'course_org': course_org,
            'all_teacher': all_teacher,
            'has_fav': has_fav
        })


class AddFavView(View):
    # 用户收藏
    def post(self, request):
        fav_id = request.POST.get('fav_id', 0)
        fav_type = request.POST.get('fav_type', 0)

        if not request.user.is_authenticated():
            res = {
                'status': 'fail',
                'msg': '用户未登录'
            }
            return HttpResponse(res, content_type='application/json')

        exist_records = UserFavorite.objects.filter(user=request, fav_id=int(fav_id), fav_type=int(fav_type))
        if exist_records:
            # 如果记录存在，则取消保存
            exist_records.delete()
            res = {
                'status': 'success',
                'msg': '收藏'
            }
            return HttpResponse(res, content_type='application/json')
        else:
            user_fav = UserFavorite()
            if int(fav_id) > 0 and int(fav_type) > 0:
                user_fav.fav_id = int(fav_id)
                user_fav.fav_type = int(fav_type)
                user_fav.save()
                res = {
                    'status': 'success',
                    'msg': '已收藏'
                }
                return HttpResponse(res, content_type='application/json')
            else:
                res = {
                    'status': 'fail',
                    'msg': '收藏出错'
                }
                return HttpResponse(res, content_type='application/json')
