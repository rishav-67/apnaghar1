from django.shortcuts import render,HttpResponseRedirect

from django.contrib.auth.forms import UserCreationForm
from .forms import user_signupk,user_logink
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import shows,contactshows,userprofile
from .models import advertisment,User
import random
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    form=advertisment.objects.all()
    formhouse=advertisment.objects.filter(category__icontains="house")
    formapartment=advertisment.objects.filter(category__icontains="apartment")
    formbanglow=advertisment.objects.filter(category__icontains="banglow")
    gk={}
    
    
    if formhouse:
        if request.method=="POST":
            form1=request.POST["search"]
            obj=advertisment.objects.filter(title__icontains=form1)
            if obj:
                return render(request,'ghar_dikhao/seachshow.html',{'obj':obj})
            else:
                messages.success(request,"no result found")
                gk.update({'formhouse':formhouse})
                
        else:
            gk.update({'formhouse':formhouse})
    if formapartment:
        if request.method=="POST":
            form1=request.POST["search"]
            obj=advertisment.objects.filter(title__icontains=form1)
            if obj:
                return render(request,'ghar_dikhao/seachshow.html',{'obj':obj})
            else:
                messages.success(request,"no result found")
                gk.update({'formapartment':formapartment})
        else:
             gk.update({'formapartment':formapartment})

    if formbanglow:
        if request.method=="POST":
            form1=request.POST["search"]
            obj=advertisment.objects.filter(title__icontains=form1)
            if obj:
                return render(request,'ghar_dikhao/seachshow.html',{'obj':obj})
            else:
                messages.success(request,"no result found")
                gk.update({'formbanglow':formbanglow})
        else:
             gk.update({'formbanglow':formbanglow})
        
    return render(request,'ghar_dikhao/home.html',{'gk':gk})
    
def user_signup(request):
    if request.method=="POST":
        form=user_signupk(request.POST)
        formnew=userprofile(request.POST)
        if form.is_valid() and formnew.is_valid():
            user=form.save()
            formx=formnew.save(commit=False)
            formx.user=user
            formx.save()
            messages.success(request,"CONGRATS!!!!! YOU HAVE SUCEESFULLY CREATED ACCOUNT")
            return HttpResponseRedirect('/signup/')
    else:
        form=user_signupk()
        formnew=userprofile()


    return render(request,'ghar_dikhao/user_signup.html',{'form':form,'formnew':formnew})
def user_login(request):
    if request.method=="POST":
        form=user_logink(request=request,data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data['username']
            upass=form.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/')
            else:
                    form=user_logink()
                    messages.success(request,"WRONG1 credential")
                    return render(request,'ghar_dikhao/user_login.html',{'form':form})
        else:
            form=user_logink()
            messages.success(request,"WRONG2 credential")
            return render(request,'ghar_dikhao/user_login.html',{'form':form})
    else:
        form=user_logink()
        return render(request,'ghar_dikhao/user_login.html',{'form':form})
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/signup/')

@login_required(login_url='/signup/')
def post(request):
    if request.method=="POST":
        form=shows(request.POST,request.FILES)
        if form.is_valid():
            title_view=request.POST['title']
            title_description=request.POST['description']
            z=request.FILES['img']
            title_category=request.POST['category']
            title_state=request.POST['state']
            title_district=request.POST['district']
            title_bedroom=request.POST['bedroom']
            xb=request.POST['balcony']
            xc=request.POST['bathroom']
            xd=request.POST['cost']
            p=request.user
            ins=advertisment(user=p,title=title_view,description=title_description,img=z,category=title_category,state=title_state,
            district=title_district,bedroom=title_bedroom,balcony=xb,bathroom=xc,cost=xd)
            ins.save()
            
            return HttpResponseRedirect('/')
        else:
            print("boooooooooooooooooooooooo")
        
    else:
        form=shows()
    return render(request,'ghar_dikhao/addavertismentadd.html',{'form':form})
        
def contact(request):
    if request.method=="POST":
        form=contactshows(request.POST)
        if form.is_valid():
            messages.success(request,"Thank You For Your Feedback")
            form.save()
            return HttpResponseRedirect('/contact/')
    else:
        form=contactshows()
    return render(request,'ghar_dikhao/contact.html',{'form':form})
@login_required(login_url='/signup/')
def yourad(request):
    form=request.user
    x=form.id
    print(x)
    obj = advertisment.objects.filter(user=form)
    print(obj)
    return render(request,'ghar_dikhao/yourad.html',{'obj':obj,'x':x,'form':form})
def searchk(request):
    return render(request,'ghar_dikhao/seachshow.html')

def about(request):
    return render(request,'ghar_dikhao/about.html')

def showselecthouse(request):
    x=5
    formhouse=advertisment.objects.filter(category__icontains="house")
    tit="house"
    
    return render(request,'ghar_dikhao/showselect.html',{'form':formhouse,'tit':tit,})


def showselectapartment(request):
    
    formapartment=advertisment.objects.filter(category__icontains="apartment")
    tit="apartment"
    
    return render(request,'ghar_dikhao/showselect.html',{'form':formapartment,'tit':tit})

def showselectbanglow(request):
    
    formbanglow=advertisment.objects.filter(category__icontains="banglow")
    tit="banglow"
    
    return render(request,'ghar_dikhao/showselect.html',{'form':formbanglow,'tit':tit})
def recent(request,check):

    form=advertisment.objects.filter(category__icontains=check).order_by('-date')

    return render(request,'ghar_dikhao/recent.html',{'form':form})
   
def oldest(request,check):
    
    form=advertisment.objects.filter(category__icontains=check).order_by('date')
    return render(request,'ghar_dikhao/recent.html',{'form':form})

def shuffle(request,check):
    
    form1=advertisment.objects.filter(category__icontains=check)
    form=list(form1)
    random.shuffle(form)
    return render(request,'ghar_dikhao/recent.html',{'form':form})
    
@login_required(login_url='/signup/')
def delete_post(request,check):
    form1=advertisment.objects.get(id=check)
    form1.delete()
    form=advertisment.objects.all()
    messages.success(request,"successfully deleted")
    return HttpResponseRedirect("/youradvertisment/")

@login_required(login_url='/signup/')
def update_post(request,check):
    if request.method=="POST":
        pi=advertisment.objects.get(pk=check)
        form=shows(request.POST,request.FILES,instance=pi)
        if form.is_valid():
            messages.success(request,"successfully EDITED")
            form.save()
            return HttpResponseRedirect("/youradvertisment/")
    else:
        pi=advertisment.objects.get(pk=check)
        form=shows(instance=pi)
    return render(request,'ghar_dikhao/update.html',{'form':form})

def information(request,check):

    form=advertisment.objects.get(pk=check)
    print(form)
    form.view_count=form.view_count+1
    form.save()
    
    form=advertisment.objects.get(pk=check)
    return render(request,'ghar_dikhao/information.html',{'form':form})
    
def delete_confirm(request,check):
    form=check
    return render(request,'ghar_dikhao/delete_confirm.html',{'form':form})