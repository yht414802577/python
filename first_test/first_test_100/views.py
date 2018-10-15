from django.shortcuts import render,HttpResponse
from . import models

# Create your views here.

def table(request):
    #DakotaRiceSalary = 36,738
    # MinervaHooperSalary = 23,789
    date_ = {
        'DakotaRiceSalary':36.738,
        'MinervaHooperSalary':23.789,
    }
    # context = {
    #     'DakotaRiceSalary':DakotaRiceSalary,
    #     'MinervaHooperSalary':MinervaHooperSalary,
    # }

    context = {
        'infortest':date_,
    }
    return render(request,'html/table.html',context)

def dashboard(request):
    return render(request, 'html/dashboard.html')

def icons(request):
    return render(request, 'html/icons.html')

def maps(request):
    return render(request, 'html/maps.html')

def notifications(request):
    return render(request, 'html/notifications.html')

def template(request):
    return render(request, 'html/template.html')

def typography(request):
    return render(request,'html/typography.html')

def upgrade(request):
    return render(request,'html/upgrade.html')

def user(request):
    if request.method == "GET":
        return render(request,'html/user.html')
    elif request.method == "POST":
        data = request.POST
        print(dir(data))

        post_company = request.POST.get('company')
        post_username = request.POST.get('username')
        post_emailaddress = request.POST.get('emailaddress')
        post_firstname = request.POST.get('firstname')
        post_lastname = request.POST.get('lastname')
        post_address = request.POST.get('address')
        post_city = request.POST.get('city')
        post_country = request.POST.get('country')
        post_postalcode = request.POST.get('postalcode')

        return render(request)