from django.shortcuts import render
from erp.models import 客戶

# Create your views here.
def dashboard(request):
    title = 'ERP SYSTEM - Dashboard'
    content_title = 'dashboard'
    return render(request, 'dashboard.html', locals())

def products(request):
    try:
        return render(request, 'products.html', locals())
    except:
        return render(request, 'products.html')

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
        
        customers = 客戶.objects.all().order_by('客戶編號')
        return render(request, 'customers.html', locals())
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
        
        customers = 客戶.objects.all().order_by('客戶編號')
        return render(request, 'customers.html', locals())
    except:
        pass 
