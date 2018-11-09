import hashlib
import io
import os
import random
import uuid

from PIL import ImageFont, ImageDraw, Image
from django.conf import settings
from django.http import HttpResponse, response, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from myapp.models import Wheel, whiteSpirit, Goods, Users

#######主页
def home(request):
    token = request.session.get('token')
    if token:
        user = Users.objects.get(token=token)
        account= user.account
    else:
        account = '未登录'

    wheels= Wheel.objects.all()
    whitespirits0 = whiteSpirit.objects.filter(typeid=0)
    whitespirits1 = whiteSpirit.objects.filter(typeid=1)
    whitespirits2 = whiteSpirit.objects.filter(typeid=2)
    whitespirits3 = whiteSpirit.objects.filter(typeid=3)
    whitespirits4 = whiteSpirit.objects.filter(typeid=4)
    whitespirits5 = whiteSpirit.objects.filter(typeid=5)

    data = {
        'wheels':wheels,
        'whitespirits0': whitespirits0,
        'whitespirits1': whitespirits1,
        'whitespirits2': whitespirits2,
        'whitespirits3': whitespirits3,
        'whitespirits4': whitespirits4,
        'whitespirits5': whitespirits5,
        'account':account
    }
    return render(request,'home.html',context=data)
####以上为主页########



###########验证码########
def verifycode(request):
    # 创建图片
    width = 80
    height = 24
    r = random.randrange(0,256)
    g = random.randrange(0,256)
    b = random.randrange(0,256)
    image = Image.new('RGB', (width, height), (r,g,b))
    # 随机数
    str = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    rand_str = ''
    for i in range(0,4):
        temp = random.randrange(0,len(str))
        rand_str += str[temp]
     # session保存验证码
    request.session['rand_str'] = rand_str
    request.session.set_expiry(60*3)
    # 创建画笔
    draw = ImageDraw.Draw(image)
    # 导入字体
    font = ImageFont.truetype('static/fonts/Fangsong.ttf',20)
    # 字体颜色
    fontcolor1 = (255, random.randrange(0,256), random.randrange(0,256))
    fontcolor2 = (255, random.randrange(0, 256), random.randrange(0, 256))
    fontcolor3 = (255, random.randrange(0, 256), random.randrange(0, 256))
    fontcolor4 = (255, random.randrange(0, 256), random.randrange(0, 256))
    # 绘制操作
    draw.text((5,2), rand_str[0], fill=fontcolor1,font=font)
    draw.text((20,2), rand_str[1], fill=fontcolor2, font=font)
    draw.text((40,2), rand_str[2], fill=fontcolor3, font=font)
    draw.text((60,2), rand_str[3], fill=fontcolor4, font=font)
    # 释放
    del draw
    #文件操作
    buff = io.BytesIO()
    image.save(buff, 'png')  # 保存在内存中
    return HttpResponse(buff.getvalue(), 'image/png')
#########以上为验证码########

def genarate_password(param):
    sha = hashlib.sha256()
    sha.update(param.encode('utf-8'))
    return sha.hexdigest()

######注册####
def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    elif request.method == 'POST':
        user = Users()
        user.account = request.POST.get('account')
        user.password = genarate_password(request.POST.get('password'))
        user.phone = request.POST.get('phone')
        user.addr = request.POST.get('addr')
        user.token = str(uuid.uuid5(uuid.uuid4(), 'register'))
        user.save()
        # 状态保持
        request.session['token'] = user.token
        return redirect('myapp:home')
######注册######


######登陆#################
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        account = request.POST.get('account')
        password = request.POST.get('password')

        print('haha')
        try:
            user = Users.objects.get(account=account)
            if user.password == genarate_password(password):  # 登录成功
                # 更新token
                user.token = str(uuid.uuid5(uuid.uuid4(), 'login'))
                user.save()
                request.session['token'] = user.token
                return redirect('myapp:home')
            else:  # 登录失败
                return render(request, 'login.html', context={'passwdErr': '密码错误!'})
        except:
            return render(request, 'login.html', context={'acountErr': '账号不存在!'})
#####以上为登陆######


### 验证校验码################
def checkVerifyCode(request):
    code = request.session.get('rand_str').lower()
    responseData = {
        'code':code,
    }
    return JsonResponse(responseData)
#########验证码验证#####

###########购物车#####
def shoppingCart(request):
    return render(request,'shoppingCart.html')
#######以上为购物车#####


#####闪购超市#####
def market(request,brandid,placeid,priceid,suitid,sortid):
    brandid = int(request.COOKIES.get('brandIndex',0))
    placeid = int(request.COOKIES.get('placeIndex',0))
    priceid = int(request.COOKIES.get('priceIndex',0))
    suitid = int(request.COOKIES.get('suitIndex',0))
    sortid = int(request.COOKIES.get('sortIndex',0))
    xfList = Goods.objects.filter(isxf=1)   #精选列表
    if brandid == 0:
        goodsList1 = Goods.objects.all()
    else:
        goodsList1 = Goods.objects.filter(brandid=brandid)
    if placeid == 0:
        goodsList2 = goodsList1
    else:
        goodsList2 = goodsList1.filter(placeid=placeid)
    if priceid == 0:
        goodsList3 = goodsList2
    else:
        goodsList3 = goodsList2.filter(priceid=priceid)
    if suitid == 0:
        goodsList4 = goodsList3
    else:
        goodsList4 = goodsList3.filter(suitid=suitid)
    if sortid == 0 or 1:
        goodsList5 = goodsList4
    elif sortid == 2:
        goodsList5 = goodsList4.order_by('saleNum')  #按销量
    elif sortid == 3:
        goodsList5 = goodsList4.order_by('price')    #按价格
    elif sortid == 4:
        goodsList5 = goodsList4.order_by('commentsNum') # 按评论数
    elif sortid == 5:
        goodsList5 = goodsList4.order_by('shelfTime')  #按上架时间排序
    elif sortid == 6:
        goodsList5 = goodsList4.filter(isspec=1)   #是否特价
    data = {
        'goodsList':goodsList5,
        'brandid':brandid,
        'placeid':placeid,
        'priceid':priceid,
        'suitid':suitid,
        'sortid':sortid,
        'xfList':xfList,
    }
    return render(request,'market.html',context=data)
#####闪购超市######################


#####账户验证#####
def checkaccount(request):
    account = request.GET.get('account')
    responseData = {
        'msg': '账号可用',
        'status': 1
    }
    try:
        user = Users.objects.get(account=account)
        responseData['msg'] = '账号已被占用'
        responseData['status'] = -1
        return JsonResponse(responseData)
    except:
        return JsonResponse(responseData)
########账号验证


#########登出#####
def logout(request):
    request.session.flush()
    return redirect('myapp:home')
########登出#######