from django.shortcuts import render,redirect
from django.contrib import messages
from app.models import Contact
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from .models import Car
from .models import Order


# Create your views here.
def base(request):
    return render(request,'base.html')

def msg(request):
    return render(request,'message.html')

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def cars(request):
    car = Car.objects.all()
    return render(request, "car.html", locals())

@login_required(login_url="/login")
def contact_us(request):
    context={}
    if request.method=='POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        sub = request.POST.get("subject")
        msg = request.POST.get("message")
        obj = Contact(name=name,email=email,subject=sub,message=msg)
        obj.save()
        context['message']=f"Dear {name},thanks for your time!"
    return render(request,'contact.html', context)

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if User.objects.filter(username = username).first():
            messages.error(request,"Username already taken")
            return redirect('signup')
        if User.objects.filter(email = email).first():
            messages.error(request,"Email already taken")
            return redirect('signup')

        if password != password2:
            messages.error(request,"Passwords do not match")
            return redirect('signup')

        myuser = User.objects.create_user(username=username,email=email,password=password)
        myuser.name = username
        myuser.save()
        messages.success(request,"Your account has been successfully created!")
        return redirect('login')
    else:
        print("error")
        return render(request,'signup.html')
    

def signin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username = loginusername,password = loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request,"Successfully logged in!")
            return redirect('index')
        else:
            messages.error(request,"Invalid credentials")
            return redirect('signup')
    else:
        print("error")
        return render(request,'login.html')
            
@login_required(login_url="/login")
def user_logout(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect('index')

@login_required(login_url="/login")
def change_password(request):
    if request.method == 'POST':
        o = request.POST.get('old')
        n = request.POST.get('new')
        c = request.POST.get('confirm')
        user = authenticate(username=request.user.username, password=o)
        if user:
            if n == c:
                user.set_password(n)
                user.save()
                messages.success(request, "Password Changed")
                return redirect('main')
            else:
                messages.success(request, "Password not matching")
                return redirect('change_pass')
        else:
            messages.success(request, "Invalid Password")
            return redirect('change_pass')
    return render(request, 'change_pass.html')

@login_required(login_url="/login")
def bill(request):
    cars = Car.objects.all()
    params = {'cars':cars}
    return render(request,'bill.html',params)

@login_required(login_url="/login")
def order(request):
    if request.method == "POST":
        billname = request.POST.get('billname','')
        billemail = request.POST.get('billemail','')
        billphone = request.POST.get('billphone','')
        billaddress = request.POST.get('billaddress','')
        billcity = request.POST.get('billcity','')
        cars11 = request.POST['cars11']
        dayss = request.POST.get('dayss','')
        date = request.POST.get('date','')
        fl = request.POST.get('fl','')
        tl = request.POST.get('tl','')
        # print(request.POST['cars11'])
        
        order = Order(name = billname,email = billemail,phone = billphone,address = billaddress,city=billcity,cars = cars11,days_for_rent = dayss,date = date,loc_from = fl,loc_to = tl)
        order.save()
        return redirect('index')
    else:
        print("error")
        return render(request,'bill.html', locals())

def admin_login(request):
    print("hiiiii")
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            print(request.user)
            return redirect('/dashboard')
        else:
            messages.error(request,'Wrong Credentials')
            return redirect('/adminlogin')
    return render(request,'adminlogin.html')

def dashboardpage(request):
    return render(request,'dashboard.html')

def admin_view(request):
    return render(request, 'adminview.html')

def add_cars(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        desc = request.POST['description']
        image = request.FILES['image']
        Car.objects.create(name=name, price=price, description=desc, image=image)
        messages.success(request, "Car added")
    return render(request, 'add_car.html', locals())

def view_cars(request):
    car = Car.objects.all()
    return render(request, 'view_car.html', locals())

def edit_cars(request, pid):
    car = Car.objects.get(id=pid)
    if request.method == "POST":
        name = request.POST['name']
        price = request.POST['price']
        desc = request.POST['description']
        try:
            image = request.FILES['image']
            car.image = image
            car.save()
        except:
            pass
        Car.objects.filter(id=pid).update(name=name, price=price, description=desc)
        messages.success(request, "Car Updated")
    return render(request, 'edit_car.html', locals())

def delete_cars(request, pid):
    car = Car.objects.get(id=pid)
    car.delete()
    messages.success(request, "Car Deleted")
    return redirect('view_car')

def admin_changepassword(request):
    if request.method == 'POST':
        o = request.POST.get('currentpassword')
        n = request.POST.get('newpassword')
        c = request.POST.get('confirmpassword')
        user = authenticate(username=request.user.username, password=o)
        if user:
            if n == c:
                user.set_password(n)
                user.save()
                messages.success(request, "Password Changed")
                return redirect('index')
            else:
                messages.success(request, "Password not matching")
                return redirect('admin_changepass')
        else:
            messages.success(request, "Invalid Password")
            return redirect('admin_changepass')
    return render(request, 'admin_changepass.html')

