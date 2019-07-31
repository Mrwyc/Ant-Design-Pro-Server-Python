from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.views import View
from User import models

# Create your views here.
import json
import ast
import hashlib


# MD5加密
def md5(arg):
    md5_str = hashlib.md5()
    b_str = arg.encode(encoding='utf-8')
    md5_str.update(b_str)
    str_md5 = md5_str.hexdigest()
    return str_md5


class StudentsView(View):

    # 如果用户账号存在则登录，不存在则创建
    def post(self, request, *args, **kwargs):
        res = {}
        data = list(request.POST.keys())[0]
        json_data = json.loads(data)
        username = json_data.get('userName', '')
        password = json_data.get('password', '')
        if username and password:
            user_queryset = models.UserModel.objects.filter(username=username).first()
            if not user_queryset:
                data = {}
                data['username'] = username
                data['password'] = md5(password)
                data['token'] = md5(username)
                models.UserModel.objects.create(**data)
                res['status'] = 'ok'
                res['currentAuthority'] = 'user'
                res['message'] = u'注册成功'
                res['token'] = md5(username)
                return JsonResponse(res)
            else:
                if md5(password) == user_queryset.password:
                    res['status'] = 'ok'
                    res['currentAuthority'] = 'user'
                    res['message'] = u'登录成功'
                    res['token'] = user_queryset.user_token
                    return JsonResponse(res)
                else:
                    res['status'] = 'error'
                    res['currentAuthority'] = 'user'
                    res['message'] = u'登录失败'
                    res['token'] = ''
                    return JsonResponse(res)
        return JsonResponse(res)

    def put(self, request, *args, **kwargs):
        return HttpResponse('PUT')

    def delete(self, request, *args, **kwargs):
        return HttpResponse('DELETE')


class RoutersData(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse([])

    def post(self, request, *args, **kwargs):
        return HttpResponse([])


class UserInfo(View):
    # 获取用户信息
    def get(self, request, *args, **kwargs):
        token_arg = request.GET.get('token', 0)
        userInfo = models.UserModel.objects.filter(user_token=token_arg).first()
        data = {
            "user": userInfo.username,
            "name": userInfo.username,
            "avatar": 'https://www.wuyongcong.com/uploads/201903/avatar_15906d9cfe68cc32_small.jpeg',
            "userid": userInfo.id,
        }
        return JsonResponse(data)


# 获取用户列表
def user_date_list(reqeust):
    userobj = models.UserModel.objects.all()
    datalist = []
    for i in userobj:
        data = {}
        data['ID'] = i.id
        data['loginNum'] = i.username
        data['token'] = i.user_token
        data['createTime'] = i.register_time.strftime("%Y-%m-%d %H:%M:%S")
        datalist.append(data)
    result = {
        'code': 200,
        'message': u'请求数据成功',
        'data': datalist
    }
    return JsonResponse(result)


class UserdataView(View):

    # 修改用户登录账号
    def post(self, request):
        result = {}
        data = list(request.POST.keys())[0]
        json_data = json.loads(data)
        try:
            user_login_num = json_data['yuanShiLogin']  # 原始登录账号
            login_num = json_data['loginNum']
        except Exception as e:
            result['message'] = u'登陆凭证过期,退出重新登录!'  # Token过期
            result['code'] = 201
            return JsonResponse(result)
        filter_data = models.UserModel.objects.filter(username=user_login_num).update(username=login_num)
        if filter_data:
            result['message'] = u'修改成功'
            result['code'] = 200
            return JsonResponse(result)
        else:
            result['message'] = u'修改失败'
            result['code'] = 201
            return JsonResponse(result)


#  删除用户
def del_user_info(request):
    result = {}
    try:
        data = list(request.POST.keys())[0]
        json_data = json.loads(data)
        models.UserModel.objects.filter(id=json_data['userID']).delete()
        result['message'] = u'删除成功'
        result['code'] = 200
    except Exception as e:
        result['message'] = u'删除失败，错误原因: {0}'.format(e)
        result['code'] = 201
    return JsonResponse(result)


def add_user_info(request):
    result = {}
    data = list(request.POST.keys())[0]
    json_data = json.loads(data)
    filter_user = models.UserModel.objects.filter(username=json_data['LoginNum'])
    if filter_user:
        result['message'] = u'当前用户已存在'
        result['code'] = 201
    else:
        if json_data['LoginNum'] and json_data['loginPwd']:
            user_data = {'username': json_data['LoginNum'],
                         'password': md5(json_data['loginPwd']),
                         'user_token': md5(json_data['LoginNum'])}
            models.UserModel.objects.create(**user_data)
            result['message'] = u'新增成功'
            result['code'] = 200
        else:
            result['message'] = u'请确定是否输入登录账号或密码'
            result['code'] = 201
    return JsonResponse(result)


def add_aritive_data(request):
    result = {}
    data = list(request.POST.keys())[0]
    json_data = json.loads(data)
    try:
        aritice_data = {
            'title': json_data['title'],
            'aritice_user': json_data['user'],
            'aritice_gjz': json_data['gjz'],
            'img_url': json_data['imgPath'],
            'content': json_data['content']
        }
        models.AriticeModel.objects.create(**aritice_data)
        result['code'] = 200
        result['message'] = u'保存成功'
    except Exception as e:
        result['code'] = 201
        result['message'] = u'保存异常: {0}'.format(e)
    return JsonResponse(result)


def get_ariticle_list(request):
    result = {}
    aritlice_list = []
    data_list = models.AriticeModel.objects.all()
    try:
        for i in data_list:
            data_dict = {}
            data_dict['ID'] = i.id
            data_dict['imgPath'] = i.img_url
            data_dict['title'] = i.title
            data_dict['user'] = i.aritice_user
            data_dict['GJZ'] = i.aritice_gjz
            data_dict['Create_Time'] = i.create_time.strftime("%Y-%m-%d %H:%M:%S")
            aritlice_list.append(data_dict)
        result['message'] = u'获取成功'
        result['code'] = 200
        result['data'] = aritlice_list
    except Exception as e:
        result['message'] = u'获取错误: {0}'.format(e)
        result['code'] = 201
    return JsonResponse(result)
