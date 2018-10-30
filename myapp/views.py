import io
import random

from PIL import ImageFont, ImageDraw, Image
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from myapp.models import User


def index(request):
    user_tel = request.COOKIES.get('user_tel')
    return render(request,'index.html',context={'user_tel':user_tel})


def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    elif request.method == 'POST':
        user_tel = request.POST.get('user_tel')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        verifycode = request.POST.get('verifycode')


        user = User()
        user.user_tel = user_tel
        user.password = password1
        if password1 == password2:
            user.password = password1
        else:
            return HttpResponse('两次密码不一致，请重新输入！')
        user.save()

        response = redirect('myapp:index')
        response.set_cookie('user_tel',user_tel)

        return response



def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        user_tel = request.POST.get('user_tel')
        password = request.POST.get('password')

    users = User.objects.filter(user_tel=user_tel).filter(password=password)
    if users.count():
        user = users.first()

        response = redirect('myapp:index')
        response.set_cookie('user_tel',user.user_tel)
        return response
    else:
        return HttpResponse('用户名或密码错误')

def verifycode(request):
    # 创建图片
    width = 110
    height = 38
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

    # 创建画笔
    draw = ImageDraw.Draw(image)

    # 添加噪点
    for i in range(0,300):
        xy = (random.randrange(0,width), random.randrange(0,height))
        fill = (random.randrange(0,256),random.randrange(0,256),random.randrange(0,256))
        draw.point(xy, fill=fill)

    # 导入字体
    font = ImageFont.truetype('static/fonts/Fangsong.ttf',25)
    # 字体颜色
    fontcolor1 = (255, random.randrange(0,256), random.randrange(0,256))
    fontcolor2 = (255, random.randrange(0, 256), random.randrange(0, 256))
    fontcolor3 = (255, random.randrange(0, 256), random.randrange(0, 256))
    fontcolor4 = (255, random.randrange(0, 256), random.randrange(0, 256))
    # 绘制操作
    draw.text((5,3), rand_str[0], fill=fontcolor1,font=font)
    draw.text((25, 3), rand_str[1], fill=fontcolor2, font=font)
    draw.text((45, 3), rand_str[2], fill=fontcolor3, font=font)
    draw.text((65, 3), rand_str[3], fill=fontcolor4, font=font)
    # 释放
    del draw
    #文件操作
    buff = io.BytesIO()
    image.save(buff, 'png') # 保存在内存中
    return HttpResponse(buff.getvalue(),'image/png')


#创建校验码
def verifynum(request):
    str1 = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    rand_str1 = ''
    for i in range(0, 4):
        temp = random.randrange(0, len(str1))
        rand_str1 += str[temp]
    return HttpResponse(rand_str1)