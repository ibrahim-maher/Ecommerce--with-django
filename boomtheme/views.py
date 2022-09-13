import re
from django.shortcuts import render

# Create your views here.
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from boomtheme import models
from json import dumps, loads
from django.http import HttpResponse
from django.contrib.auth.models import User


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def contact(request):
    return render(request, "contact.html")


def login_user(request):
    if request.method == "POST":
        user_name = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect("login")


def register(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=user_name, password=password)
            login(request, user)
            return redirect("home")
    context = {
        "form": form
    }
    return render(request, "register.html", context)


def products(request):
    return render(request, 'products.html', {"products": models.products.objects.all()})


def productDetails(request, p_id):
    product = models.products.objects.get(id=p_id)
    data = {
        "id": product.id,
        "name": product.name,
        "image1": str(product.image1),
        "image2": str(product.image2),
        "price": str(product.price)
    }
    dataJSON = dumps(data)
    return render(request, "productDetails.html", {"product": product, "data": dataJSON})


def makeOrder(request):
    if request.method == "POST":
        myDict = dict(request.POST)
        for key in myDict.keys():
            n = loads(key)
            order = models.orders(
                user=request.user.id,
                total_price=n['totalPrice'],
                total_quantity=n['totalQuantity']
            )
            order.save()
            print(order.id)
        return redirect('home')


def logout_user(request):
    logout(request)
    return redirect("login")
