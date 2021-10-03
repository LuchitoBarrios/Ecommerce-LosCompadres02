from django.shortcuts import render,HttpResponse

###

###

# Create your views here.

def home(request):

    return render(request,"newprojectapp/home.html")




def blog(request):

    return render(request,"newprojectapp/blog.html")

