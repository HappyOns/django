from django.shortcuts import render
from django.http import *
from QUser.views import *
from Shop.models import *
from django.views import View
from django.core.paginator import Paginator
from QUser.models import *
zl = GoodsType.objects.all()  # 种类

def login_valid(fun):
    def inner(request,*args,**kwargs):
        cookie_user = request.COOKIES.get("email")
        session_user = request.session.get("email")
        if cookie_user and session_user and cookie_user == session_user:
            return fun(request,*args,**kwargs)
        else:
            return HttpResponseRedirect("/Shop/login/")
    return inner

def ok(fun):
    def ook(request):
        zl = GoodsType.objects.all()
        a=fun(request)
        hd=[1,2,3,4]#首页幻灯片

        return render(request, a, locals())
    return ook


def aa(request):
    return 'buyer/Buyer1.html'
def register(request):#用户注册
    if request.method=='POST':
        us=request.POST
        name=us.get('user_name')
        password=us.get('cpwd')
        email=us.get('email')
        mak=BuyUser()
        mak.username = name
        mak.email = email
        mak.password = password
        mak.phone = None
        mak.address = None
        mak.save()
        return render(request,'buyer/login.html',locals())
    return render(request,'buyer/register.html',locals())

def login(request):#登录
    if request.method=='POST':
        # us=request.POST
        # name=us.get('user_name')
        # password=us.get('cpwd')
        # email=us.get('email')
        # mak=BuyUser()
        # mak.username = name
        # mak.email = email
        # mak.password = password
        # mak.phone = None
        # mak.address = None
        # mak.save()
        return HttpResponseRedirect('/Buyer/index', locals())
    return render(request,'buyer/login.html',locals())
def cart(request):  #购物车
    return render(request,'buyer/cart.html',locals())

def detail(request,id):#详情页
    goods = Goods.objects.get(id=int(id))
    print(goods.goods_type.id)
    return render(request,'buyer/detail.html',locals())

def list(request,id):#列表页
    goodstype=GoodsType.objects.get(id=int(id))
    if id:
        goods=goodstype.goods_set.all()
    return render(request,'buyer/list.html',locals())



def index(request):#首页
    hd=[1,2,3,4]#首页幻灯片
    zl = GoodsType.objects.all()
    return render(request, 'buyer/index.html', locals())
# Create your views here.
