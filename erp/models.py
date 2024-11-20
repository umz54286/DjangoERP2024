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


class 供應商(models.Model):
    序號 = models.AutoField(primary_key=True)
    供應商編號 = models.CharField(max_length=20)
    供應商名稱 = models.CharField(max_length=50)
    聯絡人 = models.CharField(max_length=30)
    電話 = models.CharField(max_length=20)
    地址 = models.CharField(max_length=100)
    統一編號 = models.CharField(max_length=10)

class 產品(models.Model):
    序號 = models.AutoField(primary_key=True)
    產品編號 = models.CharField(max_length=20)
    產品名稱 = models.CharField(max_length=50)
    產品描述 = models.TextField(default="")
    類別= models.CharField(max_length=20)
    單位= models.CharField(max_length=10)
    進貨成本 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    售價 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    庫存量 = models.IntegerField(default=0,null=True)
    安全庫存量 = models.IntegerField(default=0,null=True)
    供應商 = models.ForeignKey(供應商, on_delete=models.CASCADE)

class 銷售主檔(models.Model):
    序號 = models.AutoField(primary_key=True)
    銷售單號 = models.CharField(max_length=20)
    銷售日期 = models.DateField()
    付款方式 = models.CharField(max_length=20)
    運送方式 = models.CharField(max_length=20)
    備註 = models.TextField(null=True)
    狀態 = models.TextField(default='進行中')
    客戶 = models.ForeignKey(客戶, on_delete=models.CASCADE)

class 銷售明細(models.Model):
    銷售主檔 = models.OneToOneField(銷售主檔, on_delete=models.CASCADE,primary_key=True)
    產品 = models.ForeignKey(產品, on_delete=models.CASCADE)
    數量 = models.IntegerField(default=0)
    單價 = models.DecimalField(max_digits=10,decimal_places=2)
    折扣 = models.DecimalField(max_digits=10,decimal_places=2)
    金額 = models.DecimalField(max_digits=10,decimal_places=2)
    備註= models.TextField(null=True)
    
class 採購主檔(models.Model):
    序號 = models.AutoField(primary_key=True)
    採購單號 = models.CharField(max_length=20)
    採購日期 = models.DateField()
    預計到貨日期 = models.DateField()
    付款方式 = models.CharField(max_length=20)
    備註 = models.TextField(null=True)
    狀態 = models.TextField(default='進行中')
    供應商 = models.ForeignKey(供應商, on_delete=models.CASCADE)

class 採購明細(models.Model):
    採購主檔 = models.OneToOneField(採購主檔, on_delete=models.CASCADE,primary_key=True)
    產品 = models.ForeignKey(產品, on_delete=models.CASCADE)
    數量 = models.IntegerField(default=0)
    單價 = models.DecimalField(max_digits=10,decimal_places=2)
    金額 = models.DecimalField(max_digits=10,decimal_places=2)
    備註= models.TextField(null=True)

class 庫存(models.Model):
    序號 = models.AutoField(primary_key=True)
    庫存數量 = models.IntegerField(default=0)
    入庫日期 = models.DateField(null = True)
    出庫日期 = models.DateField(null = True)
    備註 = models.TextField(default="")
    產品 = models.ForeignKey(產品, on_delete=models.CASCADE)
