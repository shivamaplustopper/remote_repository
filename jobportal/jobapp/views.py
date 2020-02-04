from django.shortcuts import render
from .models import *
from .forms import *
from django.http.response import HttpResponse


def base_view(request):
    return render(request,'base.html')


# Registration View Starts
def registration_view(request):
    if request.method == "POST":
        rform = Registration_form(request.POST)
        if rform.is_valid():
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            emailid = request.POST.get('emailid')
            mobileno = request.POST.get('mobileno')
            password = request.POST.get('password')

            data = Registration_model(
                first_name=first_name,
                last_name=last_name,
                username=username,
                emailid=emailid,
                mobileno=mobileno,
                password=password,
            )
            data.save()
            rform = Registration_form()
            return render(request,'Registration.html',{'rform':rform})
        else:
            return HttpResponse('Field Missing')
    else:
        rform = Registration_form()
        return render(request,'Registration.html',{'rform':rform})

# Registration View Ends

# login View starts

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        data = Registration_model.objects.filter(username=username,password=password)
        if data:
            return render(request,'home.html')
        else:
            return HttpResponse('login unsuccessful')
    else:
        return render(request,'login.html')

#login View ends


def home_view(request):
    return render(request,'home.html')

def banglore_view(request):
    bang = Banglore_model.objects.all()
    return render(request,'banglore.html',{'bang':bang})

def hyderabad_view(request):
    hyd = Hyderabad_model.objects.all()
    return render(request,'hyderabad.html',{'hyd':hyd})

def pune_view(request):
    pune = Pune_model.objects.all()
    return render(request, 'pune.html',{'pune':pune})

def chennai_view(request):
    chennai = Chennai_model.objects.all()
    return render(request, 'chennai.html',{'chennai':chennai})