from django.shortcuts import render

# Create your views here.
def dashboard(request):
    title = 'ERP SYS - Dashboard'
    content_title = 'dashboard'
    return render(request, 'layout.html', locals())

def product(request):
    title = 'ERP SYS - 產品管理'
    content_title = '產品管理'
    content = ''
    return render(request, 'layout.html', locals())
