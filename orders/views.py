from django.shortcuts import render

# Create your views here.

def cart_show(request):
    return render(request,"cart.html")