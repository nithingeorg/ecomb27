from django.urls import path
from . import views

urlpatterns = [
    # path('', views.base, name="base"),
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('add_product/', views.add_product, name="add_product"),
    path('edit_product/<int:product_id>/', views.edit_product, name="edit_product"),
    path('delete_product/<int:product_id>/', views.delete_product, name="delete_product"),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name="add_to_cart")
]
