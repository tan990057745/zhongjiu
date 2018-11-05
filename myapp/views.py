import io
import random

from PIL import ImageFont, ImageDraw, Image
from django.http import HttpResponse, response
from django.shortcuts import render, redirect

# Create your views here.
from myapp.models import User, Wheel, whiteSpirit


def home(request):

    wheels= Wheel.objects.all()

    typeIndex = request.COOKIES.get('typeIndex',0)
    # titletypeid = TitleTypeid.objects.filter(typeid=typeIndex)
    whitespirits = whiteSpirit.objects.filter(typeid=typeIndex)

    data = {
        'wheels':wheels,
        'whitespirits':whitespirits,
    }
    return render(request,'home.html',context=data)


def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    elif request.method == 'POST':
        user_tel = request.POST.get('user_tel')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        inpverifycode = request.POST.get('inputVerifyCode')
        failVerify = request.POST.get('failVerify')
        verifycode = request.session.get('rand_str')

        # 先判断HTML产生的校验码是否输入正确
        if failVerify == "":    #为空则校验码输入正确
            #再判断后台生成的验证码是否正确输入
            if len(inpverifycode) == len(verifycode):
                for i in range(len(verifycode)):
                    if verifycode[i].lower()!=inpverifycode[i].lower():
                        return HttpResponse("验证码输入错误，请重新输入")
                else:
                    #最后判断密码输入是否OK


                    if password1 == password2:
                        user = User()
                        user.user_tel = user_tel
                        user.password = password1
                        user.save()
                        response = redirect('myapp:home')
                        response.set_cookie('user_tel', user_tel)
                        return response
                    else:
                        return HttpResponse("两次密码输入不一致，请重新输入")
            else:
                return HttpResponse("验证码输入长度错误，请重新输入")
        else:          #校验码信息不为空，则没有正确输入校验码
            return HttpResponse("请重新获取验证码并正确输入！")






######登陆#################
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        user_tel = request.POST.get('user_tel')
        password = request.POST.get('password')

    users = User.objects.filter(user_tel=user_tel).filter(password=password)
    if users.count():
        user = users.first()

        response = redirect('myapp:home')
        response.set_cookie('user_tel',user.user_tel)
        return response
    else:
        return HttpResponse('用户名或密码错误')
#####以上为登陆######



###########验证码########
def verifycode(request):
    # 创建图片
    width = 110
    height = 40
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
#########以上为验证码########



###########购物车#####
def shoppingCart(request):
    return render(request,'shoppingCart.html')
#######以上为购物车#####



########开发调试###################
def test(request):
    return render(request,'test.html')
#######以上为开发调试###############

def market(request):
    return render(request,'market.html')