from django.shortcuts import render,HttpResponse

# Create your views here.
def index(repoust):
    return render(repoust,'index.html')
