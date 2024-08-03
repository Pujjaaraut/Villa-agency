from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'TestApp/index.html')

def contact(request):
    return render(request, 'TestApp/contact.html')

def properties(request):
    return render(request, 'TestApp/properties.html')

def property_details(request): 
    return render(request, 'TestApp/property_details.html')  


def signup(request):
    if request.method=='GET':
        sform=SignupForm()
        return render(request,"LakmeApp/signup.html",{'sform':sform})
    if request.method=='POST':
        sform=SignupForm(request.POST)
        user=sform.save()
        user.set_password(user.password)
        sform=SignupForm()
        mydict={'msg':'Registration Success...','sform':sform}
        return render(request,"LakmeApp/signup.html",context=mydict)