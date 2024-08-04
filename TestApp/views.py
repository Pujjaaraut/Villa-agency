from django.shortcuts import render
from django.http import HttpResponse
from .forms import MyModelForm
from .forms import SignupForm
from django.shortcuts import redirect
from .models import Contact

# Create your views here.
def index(request):
    return render(request, 'TestApp/index.html')

def contact(request):
    return render(request, 'TestApp/contact.html')

def properties(request):
    return render(request, 'TestApp/properties.html')

def property_details(request): 
    return render(request, 'TestApp/property_details.html')  
    
def Signup(request):
    if request.method=='GET':
        sform=SignupForm()
        return render(request,"TestApp/Signup.html",{'sform':sform})
    if request.method=='POST':
        sform=SignupForm(request.POST)
        user=sform.save()
        user.set_password(user.password)
        sform=SignupForm()
        mydict={'msg':'Registration Success...','sform':sform}
        return render(request,"TestApp/Signup.html",context=mydict)
    
def contact(request):
    if request.method == "POST":
        Fullname = request.POST.get('Fullname')
        Email = request.POST.get('Email')
        Sub = request.POST.get('Sub')
        message = request.POST.get('message')
        
        # Ensure your model fields match these names
        en = Contact(Fullname=Fullname, Email=Email, Sub=Sub, message=message)
        en.save()
        
        return render(request, 'contact.html', {'success': True})
    else:
        return render(request, 'TestApp/contact.html')  

def my_view(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index/')
    else:
        form = MyModelForm()
    return render(request, 'TestApp/my_template.html',{'form':form})