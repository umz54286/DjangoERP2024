from django.db import models

# Create your models here.


class 客戶(models.Model):
    序號 = models.AutoField(primary_key=True, null=False)
    客戶編號 = models.CharField(max_length=20)
    客戶名稱 = models.CharField(max_length=50)
    聯絡人 = models.CharField(max_length=30)
    電話 = models.CharField(max_length=20)
    地址 = models.CharField(max_length=100)
    統一編號 = models.CharField(max_length=10)
    信用額度 = models.IntegerField
    備註 = models.TextField


class 供應商(models.Model):
    序號 = models.AutoField(primary_key=True)
    供應商編號 = models.CharField(max_length=20)
    供應商名稱 = models.CharField(max_length=50)
    聯絡人 = models.CharField(max_length=30)
    電話 = models.CharField(max_length=20)
    地址 = models.CharField(max_length=100)
    統一編號 = models.CharField(max_length=10)
    備註 = models.TextField

    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
