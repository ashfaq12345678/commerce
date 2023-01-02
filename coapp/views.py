from django.shortcuts import render
from django.db.models import Count
from django.views import View
from django.http import HttpResponse
from . models import Product

# from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, "app/home.html" )
def about(request):
    return render(request, "app/about.html" )
def contact(request):
    return render(request, "app/contact.html" )



class CategoryView(View) :
  def get(self,request, val):
    # products=Product.objects.filter(category=val).values_list('title', 'product_image','discounted_price') #flat=True)
    products= Product.objects.filter(category=val)
    title = Product.objects.filter(category=val).values('title')
    return render (request,'app/category.html', locals())
    # locals() is a built-in function to pass all the local variables from a function to the html page here category page
class CategoryTitle(View):
  def get(self,request, val):
     products= Product.objects.filter(title=val)
     title = Product.objects.filter(category=products[0].category).values('title')
     return render (request,'app/category.html', locals())



class ProductDetail(View):
   def get(self,request, pk):
       products= Product.objects.get(pk=pk)
       return render (request,'app/productdetail.html', locals())
