from django.shortcuts import render

# Create your views here.
def dashboard(request):
    title = 'ERP SYSTEM - Dashboard'
    content_title = 'dashboard'
    return render(request, 'layout.html', locals())

def product(request):
    title = 'ERP SYSTEM - 產品管理'
    content_title = '產品管理'
    content = ''
    try:
        return render(request, 'layout.html', locals())
    except:
        return render(request, 'layout.html')
    
