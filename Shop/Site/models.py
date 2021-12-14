from django.db import models
from django.db.models.deletion import PROTECT
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=30,verbose_name="Название категории",null=True,blank=False)
    photo = models.ImageField(verbose_name="Фотография",null=True,blank=False)

    class Meta:
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"
        ordering = ['id']

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

class Clothes(models.Model):
    garment = models.ForeignKey(Categories,on_delete=models.CASCADE,null = True)
    name = models.CharField(max_length=100,verbose_name="Название вещи",null=True,blank=False)
    price = models.PositiveIntegerField(verbose_name='Цена',null=True,blank=False)
    photo = models.ImageField(verbose_name="Фотография",null=True,blank=False)
    
    class Meta:
        verbose_name = "элемент одежды"
        verbose_name_plural = "Одежда"
        ordering = ['id']

    def __str__(self):
        return self.name


from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Заказы пользователей"
        ordering = ['id']


def post_save_profile_create(sender,instance,created,*args,**kwargs):
    if created:
        Profile.objects.get_or_create(user = instance)

post_save.connect(post_save_profile_create,sender = settings.AUTH_USER_MODEL)



class Profile_Cart(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    item = models.OneToOneField(Clothes,on_delete = models.CASCADE)
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['id']


class Favourite(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    item = models.OneToOneField(Clothes,on_delete = models.CASCADE)

import datetime
class Orders(models.Model):
    STATUS = (
        ('NR', 'Формируется'),
        ('R', 'Готов'),
    )

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ['id']
    user = models.ForeignKey(Profile,verbose_name="Покупатель",null = False,on_delete = models.CASCADE)
    status = models.CharField(max_length=2, verbose_name="Статус заказа",choices=STATUS,default='NR')
    data_field = models.DateField(verbose_name = 'Дата',auto_now_add = True)
    order_price = models.IntegerField(verbose_name = 'Сумма заказа',editable = False)


class Order(models.Model):
    order_id = models.ForeignKey(Orders,verbose_name = '"ID заказа"',on_delete=models.CASCADE)
    item = models.ForeignKey(Clothes,verbose_name = '"ID предмета"',on_delete=models.CASCADE)  

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ['id']
        unique_together = [("order_id", "item")]