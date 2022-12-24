from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from . models import Product
# from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, "app/home.html")

class CategoryView(View) :
  def get(self,request, val):
    product=Product.objects.filter(category=val).values().title
    return render (request,'app/category.html', locals())
    # locals() is a built-in function to pass all the local variables from a function to the html page here category page

