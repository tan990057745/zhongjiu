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


#创建商城商品列表
class Goods(models.Model):
    img = models.CharField(max_length=256)  #图片
    name = models.CharField(max_length=100) #名字
    price = models.CharField(max_length=100) #价格
    saleNum = models.IntegerField()         #销量
    commentsNum = models.CharField(max_length=100)   #评论数量

    isxf = models.CharField(max_length=10)         #是否优选
    isspec = models.CharField(max_length=10)       #是否特价
    brandid = models.CharField(max_length=10)       #品牌ID
    placeid = models.CharField(max_length=10)       #产地
    priceid = models.CharField(max_length=10)       #价格
    suitid = models.CharField(max_length=10)        #适用ID
    sortid = models.CharField(max_length=10)        #按照什么排序
    shelfTime = models.TimeField()                  #上架时间

    class Meta:
        db_table='zj_market'






