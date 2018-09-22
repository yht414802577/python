from django.shortcuts import render


# Create your views here.

def remove(request):
    context = {
        'num':'aaa',
        'moblie':'111111',
        'liu':'liu',
    }

    return render(request,'index.html',context)
