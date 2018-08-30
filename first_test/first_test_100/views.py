from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
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