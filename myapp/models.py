from django.db import models

# Create your models here.
class User(models.Model):
    user_tel = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Base(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=10)
    class Meta:
        abstract = True

class Wheel(Base):
    class Meta:
        db_table='zj_wheel'

# 首页商品白酒切换展示
# "img":"img/floor_liquor1.jpg",
# 			"id":11,
# 			"name":"52°泸州老窖头曲500ml",
# 			"price":"￥129.00",
# 			"small":{
# 					"img1":"img/floor_liquor1.jpg",
# 					"img2":"img/floor_liquor1 (2).jpg",
# 					"img3":"img/floor_liquor1 (3).jpg",
# 					"img4":"img/floor_liquor1 (4).jpg",
# # 					"img5":"img/floor_liquor1 (5).jpg"
# 			}

class HomeShow(models.Model):
    img = models.CharField(max_length=100)        #图片
    productid = models.CharField(max_length=10)   #产品ID
    name = models.CharField(max_length=100)       #名字
    price = models.DecimalField(max_digits=7, decimal_places=2)   #价格
    typeid = models.CharField(max_length=10)      #分类ID
    class Meta:
        abstract = True

class whiteSpirit(HomeShow):
    class Meta:
        db_table = 'zj_whiteSpirit'

# # 创建商品分类表格
# class TitleTypeid(models.Model):
#     titlename = models.CharField(max_length=100)
#     typeid = models.CharField(max_length=10)