from django.shortcuts import render, redirect
from erp.models import 客戶, 供應商, 產品, 銷售主檔, 銷售明細, 採購主檔, 採購明細, 庫存
from datetime import date

# Create your views here.
def dashboard(request):
    title = 'ERP SYSTEM - Dashboard'
    content_title = 'dashboard'
    return render(request, 'dashboard.html', locals())


def products(request):
    try:
        products = 產品.objects.select_related('供應商').order_by('產品編號')
        return render(request, 'products.html', locals())
    except:
        return render(request, 'products.html')

def insertProducts(request):
    try:
        supplier = 供應商.objects.get(供應商名稱 = request.POST['Isupplier'])

        unit = 產品.objects.create(產品編號 = request.POST['IproductCode'], 產品名稱 = request.POST['IproductName'], 產品描述 = request.POST['IproductDescription'], 類別 = request.POST['Icategory'] , 單位 = request.POST['Iunit'] , 供應商 = supplier)
        
        unit.save()
        
        return redirect('/products')
    except:               
        pass 

def modifyProducts(request):
    try:
        unit = 產品.objects.get(產品編號 = request.POST['MproductCode'])
        unit.產品名稱 = request.POST['MproductName']
        unit.產品描述 = request.POST['MproductDescription']
        unit.類別 = request.POST['Mcategory']
        unit.單位 = request.POST['Munit']   
        unit.save()
        
        return redirect('/products')
    except:
        pass 

def purchaseOrders(request):
    try:
        purchaseOrders = 採購主檔.objects.select_related('採購明細','供應商').order_by('採購單號')
        return render(request, 'purchaseOrders.html', locals())
    except:
        pass

def insertPurchaseOrders(request):
    try:
        supplier = 供應商.objects.get(供應商名稱 = request.POST['Isupplier'])

        unit = 採購主檔.objects.create(採購單號 = request.POST['IpurchaseOrderCode'], 採購日期 = request.POST['IpurchaseDate'], 預計到貨日期 = request.POST['IarriveDate'], 付款方式 = request.POST['Ipayment'] , 備註 = request.POST['Inote'] , 供應商 = supplier)
        
        unit.save()

        purchaseOrder = 採購主檔.objects.get(採購單號 = request.POST['IpurchaseOrderCode'])

        product = 產品.objects.get(產品編號 = request.POST['IpurchaseProduct'])

        unit = 採購明細.objects.create(採購主檔 = purchaseOrder, 產品 = product, 數量 = request.POST['IpurchaseQuantity'], 單價 = request.POST['IunitPrice'] , 金額 = request.POST['Iamount'])

        unit.save()

        return redirect('/purchaseOrders')
    except:               
        pass 

def modifyPurchaseOrders(request):
    try:
        # 供應商
        supplier = 供應商.objects.get(供應商名稱 = request.POST['Msupplier'])

        # 主檔
        purchaseOrder = 採購主檔.objects.get(採購單號 = request.POST['MpurchaseOrderCode'])
        purchaseOrder.採購日期 = request.POST['MpurchaseDate']
        purchaseOrder.預計到貨日期 = request.POST['MarriveDate']
        purchaseOrder.付款方式 = request.POST['Mpayment']
        purchaseOrder.供應商 = supplier
        purchaseOrder.狀態 = request.POST['Mstatus']  
        purchaseOrder.備註 = request.POST['Mremark']      
        purchaseOrder.save()

        # 產品
        product = 產品.objects.get(產品編號 = request.POST['MpurchaseProduct'])

        # 明細
        unit = 採購明細.objects.get(採購主檔 = purchaseOrder)
        unit.數量 = request.POST['MpurchaseQuantity']
        unit.單價 = request.POST['MunitPrice']
        unit.金額 = request.POST['Mamount']
        unit.產品 = product
        unit.save()
        
        return redirect('/purchaseOrders')
    except:
        pass 


def suppliers(request):
    try:
        suppliers = 供應商.objects.all().order_by('供應商編號')
        return render(request, 'suppliers.html', locals())
    except:
        pass
    
def insertSuppliers(request):
    try:
        unit = 供應商.objects.create(供應商編號 = request.POST['IsupplierCode'], 供應商名稱 = request.POST['IsupplierName'], 聯絡人 = request.POST['IcontactPerson'], 電話 = request.POST['Iphone'] , 地址 = request.POST['Iaddress'] , 統一編號 = request.POST['IunifiedNumber'])
        unit.save()
        
        return redirect('/suppliers')
    except:               
        pass 

def modifySuppliers(request):
    try:
        unit = 供應商.objects.get(統一編號 = request.POST['MunifiedNumber'])
        unit.供應商編號 = request.POST['MsupplierCode']
        unit.供應商名稱 = request.POST['MsupplierName']
        unit.聯絡人 = request.POST['McontactPerson']
        unit.電話 = request.POST['Mphone']
        unit.地址 = request.POST['Maddress']      
        unit.save()
        
        return redirect('/suppliers')
    except:
        pass 

def orders(request):
    try:
        orders = 銷售主檔.objects.select_related('銷售明細','客戶')
        sellProducts = 銷售明細.objects.select_related('產品')
        return render(request, 'orders.html', locals())
    except:
        pass

def customers(request):
    try:
        customers = 客戶.objects.all().order_by('客戶編號')
        return render(request, 'customers.html', locals())
    except:
        return render(request, 'customers.html')
    
def insertCustomers(request):
    try:
        unit = 客戶.objects.create(客戶編號 = request.POST['IcustomerCode'], 客戶名稱 = request.POST['IcustomerName'], 聯絡人 = request.POST['IcontactPerson'], 電話 = request.POST['Iphone'] , 地址 = request.POST['Iaddress'] , 統一編號 = request.POST['IunifiedNumber'])
        
        unit.save()
        return redirect('/customers')
    except:               
        pass 

def modifyCustomers(request):
    try:
        unit = 客戶.objects.get(統一編號 = request.POST['MunifiedNumber'])
        unit.客戶編號 = request.POST['McustomerCode']
        unit.客戶名稱 = request.POST['McustomerName']
        unit.聯絡人 = request.POST['McontactPerson']
        unit.電話 = request.POST['Mphone']
        unit.地址 = request.POST['Maddress']      
        unit.save()
        
        return redirect('/customers')
    except:
        pass

def inventories(request):
    try:
        inventories = 庫存.objects.select_related('產品')
        return render(request, 'inventories.html', locals())
    except:
        pass

def entry(request):
    try:
        purchaseOrders = 採購主檔.objects.select_related('採購明細','供應商').filter(狀態='已核准').order_by('採購單號')
        today = date.today()
        return render(request, 'entry.html', locals())
    except:
        pass


def createEntry(request):
    try:
        product = 產品.objects.get(產品編號 = request.POST['purchaseProduct'])
        unit = 庫存.objects.create(庫存數量 = request.POST['purchaseQuantity'], 入庫日期 = request.POST['arriveDate'], 備註 = '採購入庫', 產品 = product)
        unit.save()

        purchaseOrder = 採購主檔.objects.get(採購單號 = request.POST['purchaseOrderCode'])
        purchaseOrder.狀態 = '已入庫'
        purchaseOrder.save()

        return redirect('/entry')
    except:               
        pass


def delivery(request):
    try:
        orders = 銷售主檔.objects.select_related('銷售明細','客戶').filter(狀態='已核准').order_by('銷售單號')
        today = date.today()
        return render(request, 'delivery.html', locals())
    except:
        pass

def createDelivery(request):
    try:
        product = 產品.objects.get(產品編號 = request.POST['sellProduct'])
        unit = 庫存.objects.create(庫存數量 = -int(request.POST['sellQuantity']), 出庫日期 = request.POST['deliveryDate'], 備註 = '銷貨出庫', 產品 = product)
        unit.save()

        order = 銷售主檔.objects.get(銷售單號 = request.POST['orderCode'])
        order.狀態 = '已出庫'
        order.save()
        return redirect('/delivery')
    except:               
        pass

# 要修改    

def insertOrders(request):
    try:
        unit = 客戶.objects.create(客戶編號 = request.POST['IcustomerCode'], 客戶名稱 = request.POST['IcustomerName'], 聯絡人 = request.POST['IcontactPerson'], 電話 = request.POST['Iphone'] , 地址 = request.POST['Iaddress'] , 統一編號 = request.POST['IunifiedNumber'])
        
        unit.save()
        
        customers = 客戶.objects.all().order_by('客戶編號')
        return render(request, 'orders.html', locals())
    except:               
        pass 

def modifyOrders(request):
    try:
        unit = 客戶.objects.get(統一編號 = request.POST['MunifiedNumber'])
        unit.客戶編號 = request.POST['McustomerCode']
        unit.客戶名稱 = request.POST['McustomerName']
        unit.聯絡人 = request.POST['McontactPerson']
        unit.電話 = request.POST['Mphone']
        unit.地址 = request.POST['Maddress']      
        unit.save()
        
        customers = 客戶.objects.all().order_by('客戶編號')
        return render(request, 'orders.html', locals())
    except:
        pass 




def inventoryReport(request):
    try:
        inventoryReport = 庫存.objects.select_related('產品')

        # inventoryReport = 庫存.objects.all()
        # unit = 客戶.objects.get(統一編號 = request.POST['MunifiedNumber'])

        
        return render(request, 'inventoryReport.html', locals())
    except:
        pass
    
