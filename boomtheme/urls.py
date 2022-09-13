from django.urls import path
from boomtheme import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('contact/', views.contact, name="contact"),
    path('login/', views.login_user, name="login"),
    path('register/', views.register, name="register"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('products/', views.products, name="products"),
    path('product/<int:p_id>/', views.productDetails, name="productDetails"),
    path('order', views.makeOrder, name="order"),
    path('logout/', views.logout_user, name="logout"),

]
