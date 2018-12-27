from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.
'''
def index(request):
    return HttpResponse("Hello Django!")
'''

def index(request):
    return render (request,"index.html")

'''
def add(request,a,b):
    s = int(a)+int(b)
    return HttpResponse(str(s))
'''
#登錄動作
def login_action(request):
    if request.method =='POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username = username,password = password)
        #if username =='admin' and password == 'admin123':
        if user is not None:
            auth.login(request,user) #登錄
            #return HttpResponse('login success!')
            #return HttpResponseRedirect('/event_manage/')
            request.session['user'] = username #將session資訊紀錄到瀏覽器
            response = HttpResponseRedirect('/event_manage/')
            #response.set_cookie('user',username,3600) #新增瀏覽器cookie
            return response
        else:
            return render(request,'index.html',{'error': 'username or password error!'})

#發佈會管理
@login_required
def event_manage(request):
    #username = request.COOKIES.get('user','') #讀取瀏覽器cookie
    username = request.session.get('user','')  #讀取瀏覽器session
    return render(request,"event_manage.html",{"user":username})
