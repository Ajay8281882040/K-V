from django.shortcuts import render
from django.http import HttpResponse
from.models import Product
def index(request):
    products=Product.objects.all()
    return  render(request,'index.html',{'products':products})
  #return HttpResponse("<h1><center>welcome </center></h1>")
def about(request):
    return HttpResponse("<h1><center>ABOUT US</center></h1>")
def contact(request):
    return HttpResponse("<h1><center>CONTACT US</center><h1>")
