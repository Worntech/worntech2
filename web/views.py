from typing import Counter
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

from django.conf import settings
from django.core.mail import send_mail

from . models import *
from . forms import *

# Create your views here.
def signup(request):
    form = MyUserForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        # password2 = request.POST.get('password2')
        
        form = MyUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
    contex = {"form":form}

        # if password == password2:
        #     if MyUser.objects.filter(email=email).exists():
        #         messages.success(request, f"Email {email} Already Taken")
        #         return redirect('signup')
        #     elif MyUser.objects.filter(username=username).exists():
        #         messages.success(request, f"Username {username} Already Taken")
        #         return redirect('signup')
        #     else:
        #         user = MyUser.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, phone=phone,  password=password)
        #         user.save()



                # #log user in and redirect to settings page
                # user_login = auth.authenticate(username=username, password=password)
                # auth.login(request, user_login)

                
    #             return redirect('signin')
    #     else:
    #         messages.success(request, 'The Passwords Not Matching')
    #         return redirect('signup')

    # else:
    
    return render(request, 'signup.html',contex)
    
def signin(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.success(request, 'Credentials Invalid')
            return redirect('signin')

    else:
        return render(request, 'signin.html')

def logout(request):
    auth.logout(request)
    return redirect('signin')


def index(request):
    service = Service.objects.all()
    context={
        
        "service":service
    }
    return render(request, 'index.html',context)
def requestService(request):
    requestservice = Projectorder()
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        project_type = request.POST.get('project_type')
        project_name = request.POST.get('project_name')
        company_name = request.POST.get('company_name')
        project_description = request.POST.get('project_description')
        requestservice = ProjectorderForm(request.POST, files=request.FILES)
        if requestservice.is_valid():
            requestservice.save()
            
            # sending email to user
            # username = request.user.username
            #last_name = request.POST['last_name']
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = "Welcome to (World in Innovation With Technology(WORNTECH)"
            message = f"Thanks  {name} for sending message to us, we will answer your soon as possible, enjoy the service with WORNTECH The technology center"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=True)
            #messages.success(request,f"Message Sent Successfully to {to_dimoso_email} - DIMOSO ELECTRONICS CENTER Manager ")
            return redirect('requestService')
            #return redirect('index')
        # email end

    context={
        "requestservice":requestservice
    }
    return render(request, 'requestService.html', context)
def services(request):
    return render(request, 'services.html')
def about(request):
    about1 = About.objects.all()
    context={
        
        "about1":about1
    }
    
    return render(request, 'about.html',context)
def news(request):
    return render(request, 'news.html')
def elements(request):
    return render(request, 'elements.html')
def userview(request):
    form = AboutForm()
    if request.method == "POST":
        form = AboutForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('userview')
            about1 = About.objects.all()
            context={
                "form":form,
                "about1":about1
            }
            return render(request, 'userview.html',context)
    else:
        about1 = About.objects.all()
        context={
            "form":form,
            "about1":about1
        }
        
        return render(request, 'userview.html',context)
    
    
    
def userview(request):
    form = AboutForm()
    if request.method == "POST":
        form = AboutForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('userview')
        
    service = ServiceForm()
    if request.method == "POST":
        service = ServiceForm(request.POST, files=request.FILES)
        if service.is_valid():
            service.save()
            return redirect('userview')

    context={
        "service":service,
        "form":form,
    }
        
    return render(request, 'userview.html',context)
def contact(request):
    message1 = MessageForm()
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        phone = request.POST.get('phone')
        message1 = MessageForm(request.POST, files=request.FILES)
        if message1.is_valid():
            message1.save()
            return redirect('contact')

    context={
        "message1":message1
    }
    return render(request, 'contact.html', context)


# view used in message of contact us
def message(request):
    message1 = Message.objects.all()
    context={
        "message1":message1
    }
        
    return render(request, 'message.html', context)
    #end of the contact message view

def innovation(request):
    return render(request, 'innovation.html')
def projecthub(request):
    return render(request, 'projecthub.html')

# view messages
def viewmessage(request, id):
    message = Message.objects.get(id=id)
    
    context = {"message":message}
    return render(request, 'viewmessage.html', context)
def deletemessage(request, id):
    message = Message.objects.get(id=id)
    if request.method == "POST":
        message.delete()
        return redirect('message')
    
    context = {"message":message}
    return render(request, 'deletemessage.html', context)

# view services
def viewservice(request, id):
    service = Service.objects.get(id=id)
    
    context = {"service":service}
    return render(request, 'viewservice.html', context)

# update service
def updateservice(request, id):
    e = Service.objects.get(id=id)
    service = ServiceForm(instance=e)
    if request.method == "POST":
        service = ServiceForm(request.POST, files=request.FILES, instance=e)
        if service.is_valid():
            service.save()
            return redirect('index')
    context = {"service":service}
    return render(request, 'updateservice.html', context)

# delete service
def deleteservice(request, id):
    service = Service.objects.get(id=id)
    if request.method == "POST":
        service.delete()
        return redirect('index')
    
    context = {"service":service}
    return render(request, 'deleteservice.html', context)

        #  for admin pages   
def base(request):
    return render(request, 'base.html')
def dashboard(request):
    message1 = Message.objects.all()
    projectorder = Projectorder.objects.all()
    
    
    total_message = message1.count()
    total_projectorder = projectorder.count()
    context={
        "total_message":total_message,
        "total_projectorder":total_projectorder
    }
    return render(request, 'dashboard.html', context)
def tables(request):
    return render(request, 'tables.html')
def admin1(request):
    return render(request, 'admin1.html')
def billing(request):
    return render(request, 'billing.html')

def registereduser(request):
    return render(request, 'registereduser.html')
def innovation(request):
    return render(request, 'innovation.html')
def uploadfile(request):
    return render(request, 'uploadfile.html')
def uploadproject(request):
    return render(request, 'uploadproject.html')
def uploadtutorial(request):
    return render(request, 'uploadtutorial.html')
def projectorder(request):
    projectorder = Projectorder.objects.all()
    context={
        "projectorder":projectorder,
    }
        
    return render(request, 'projectorder.html', context)

# view project order
def viewprojectorder(request, id):
    projectorder = Projectorder.objects.get(id=id)
    
    context = {"projectorder":projectorder}
    return render(request, 'viewprojectorder.html', context)

# delete projectorder
def deleteprojectorder(request, id):
    projectorder = Projectorder.objects.get(id=id)
    if request.method == "POST":
        projectorder.delete()
        return redirect('projectorder')
    
    context = {"projectorder":projectorder}
    return render(request, 'deleteprojectorder.html', context)
