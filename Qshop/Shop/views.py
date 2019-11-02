from django.shortcuts import render
from django.http import *
from QUser.views import *
from Shop.models import *
from django.views import View
from django.core.paginator import Paginator
from Qshop.settings import PAZE_SIZE
class GoodsView(View):
    def get(self,request):
        result={
            "version": 'v1',
            'code': '200',
            'data': [],
            'page_range': [],
            "referer": "",
        }
        id = request.GET.get("id")  # 尝试获取前端get提交的id
        # 如果id 存在,获取当前id 的数据
        if id:
            goods_data = Goods.objects.get(id=int(id))
            result["data"].append(
                {"id": goods_data.id,
                 "name": goods_data.name,
                 "price": goods_data.price,
                 "number": goods_data.number,
                 "production": goods_data.production,
                 "safe_date": goods_data.safe_date,
                 "picture": goods_data.picture.url,
                 "description": goods_data.description,
                 "statue": goods_data.statue
                 }
            )
        else:
            # 尝试获取页码,如果页码不存在,默认第一页
            page_number = request.GET.get("page", 1)
            # 尝试获取查询的值
            keywords = request.GET.get("keywords")
            # 获取数据
            all_goods = Goods.objects.all()
            if keywords:  # 如果有值,查询对应值
                all_goods = Goods.objects.filter(name__contains=keywords)
                result["referer"] = "&keywords=%s" % keywords
            # 进行分页
            paginator = Paginator(all_goods, 2)
            # 获取单页数据
            page_data = paginator.page(page_number)
            result["page_range"] = list(paginator.page_range)
            goods_data = [
                {"id": g.id,
                 "name": g.name,
                 "price": g.price,
                 "number": g.number,
                 "production": g.production,
                 "safe_date": g.safe_date,
                 "picture": g.picture.url,
                 "description": g.description,
                 "statue": g.statue
                 } for g in page_data
            ]
            result["data"] = goods_data
        return JsonResponse(result)
def vue_list_goods(request):
    return render(request,'shop/vue_list_goods.html')
def goods(request,id):
    goods_list=Goods.objects.get(id=int(id))
    return render(request,'shop/xq_goods.html',locals())
def set_goods(request,id):
    set_type=request.GET.get('set_type')
    goods=Goods.objects.get(id=int(id))
    if set_type=='up':
        goods.statue=1
    else:
        goods.statue=0
    goods.save()
    return HttpResponseRedirect('/Shop/list_goods')
def list_goods(request):
    goods_list=Goods.objects.all()
    return render(request,'shop/list_goods.html',locals())
def add_goods(request,id=None):
    hhh=None
    if id :
        goods_list=Goods.objects.get(id=int(id))
        hhh,kkk='text','修改信息'
    else:
        hhh ,kkk= 'datetime-local','添加商品'
    #添加商品
    if request.method=='POST':
        ok=request.POST
        name=ok.get('name')
        price = ok.get('price')
        number = ok.get('number')
        production = ok.get('production')
        safe_date = ok.get('safe_date')
        picture = request.FILES.get('picture')
        description = ok.get('description')
        shop = Goods()
        if hhh=='text':
            production=production.replace('年','-').replace('月','-').replace('日','')
            shop=Goods.objects.get(id=int(id))
        shop.name=name
        shop.price=price
        shop.production=production
        shop.safe_date =safe_date
        if picture:
            shop. picture=picture
        shop. description=description
        shop.number=number
        shop.statue=0
        shop.save()
        return HttpResponseRedirect((lambda : '/Shop/goods/{}'.format(id) if id else '/Shop/list_goods/')())


    return render(request,'shop/add_goods.html',locals())
def profile(request):
    user_email=request.COOKIES.get("email")
    user=Quser.objects.get(email=user_email)
    return render(request,'shop/profile.html',{'user':user})

def set_profile(request):
    user_email=request.COOKIES.get("email")
    user=Quser.objects.get(email=user_email)
    if request.method=='POST':
        post_data=request.POST
        username=post_data.get('username')
        gender=post_data.get('gender')
        age=post_data.get('age')
        phone=post_data.get('phone')
        address=post_data.get('address')
        user.username=username
        user.gender=gender
        user.age=age
        user.phone=phone
        user.address=address
        user.save()
        return HttpResponseRedirect('/Shop/profile')
    return render(request,'shop/set_profile.html',{'user':user})

#校验登录
def login_valid(fun):
    def inner(request,*args,**kwargs):
        cookie_user = request.COOKIES.get("email")
        session_user = request.session.get("email")
        if cookie_user and session_user and cookie_user == session_user:
            return fun(request,*args,**kwargs)
        else:
            return HttpResponseRedirect("/Shop/login/")
    return inner

def register(request):
    """
    后台卖家注册功能
    """
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # 检测用户是否注册过
        # 注册过，提示当前邮箱已经注册
        error = ""
        if valid_user(email):
            error = "当前邮箱已经注册"
        #没有注册过
        else:
            # 对密码加密
            password = set_password(password)
            #保存到数据库
            add_user(email = email,password = password)
            #跳转到登录
            return HttpResponseRedirect("/Shop/login/")
    return render(request,"shop/register.html",locals())


def login(request):
    """
    后台卖家登录功能
    """
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        #判断用户是否存在
        # 如果存在
        user = valid_user(email)
        if user:
            #判断密码是否正确
            db_password = user.password
            request_password = set_password(password)
            if db_password == request_password:
                response = HttpResponseRedirect("/Shop/")
                response.set_cookie("email",user.email)
                response.set_cookie("user_id", user.id)
                request.session["email"] = user.email
                return response
            else:
                error = "密码错误"
        else:
            error = "用户不存在"
    return render(request,"shop/login.html",locals())

@login_valid
def index(request):
    """
    后台卖家首页
    """
    return render(request,"shop/index.html")

def logout(request):
    """
    后台卖家退出登录功能
    """
    response = HttpResponseRedirect("/Shop/login/")
    response.delete_cookie("email")
    response.delete_cookie("user_id")
    request.session.clear()
    return response


def forget_password(request):
    """
    后台卖家忘记密码功能
    """
    return render(request,"shop/forgot-password.html")

def resest_password(request):
    """
        重置密码
    :param request:
    :return:
    """
    if request.method=="POST":
        email=request.POST.get('email')
        if email and valid_user(email):
            #发送邮件内容
            #首先需要有找回页面的地址
            #其次包括要修改的密码账号
            #再次包干修改时的一个校验码
                #使用当前时间+账号   ==>进行md5加密
            hash_code=set_password(email)
            content='127.0.0.1:8000/Shop/change_password/?email=%s&token=%s'%(email,hash_code)
            'sendmail'
    return HttpResponseRedirect('/Shop/forget_password')

def change_password(request):
    email=request.GET.get('email')
    token=request.GET.get('token')
    now_token=set_password(email)
    if valid_user(email) and now_token==token:
        return render(request,'shop/change_password.html')
    else:
        return HttpResponseRedirect('/Shop/forget_password/')
# Create your views here.
