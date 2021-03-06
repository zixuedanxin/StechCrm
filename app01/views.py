from django.shortcuts import render,HttpResponse,redirect

from rbac import models
from rbac.service.init_permission import init_permission
# Create your views here.

def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        name=request.POST.get('username')
        pwd=request.POST.get('password')
        print(name,pwd)
        user=models.User.objects.filter(username=name,password=pwd).first()
        if user:
            print(user.userinfo)
            request.session['user']={'username':name,'id':user.id,'userinfo_id':user.userinfo.id,'uname':user.userinfo.name}
            init_permission(user,request)
            return redirect('/index/')
        return redirect('/login/')


def index(request):
    return render(request,'index.html')