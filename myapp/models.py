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