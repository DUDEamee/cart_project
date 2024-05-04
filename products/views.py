from django.shortcuts import render
from . models import product
# Create your views here.

def index(request):
    return render(request,'index.html')

def list_products(request):

    product_list=product.objects.all()
    context={"products":product_list}

    return render(request,'products.html',context)

def detail_products(request):
    return render(request,'product_details.html')