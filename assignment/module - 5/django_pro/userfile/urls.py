from django.urls import path
from.import views

urlpatterns = [
    path('',views.index,name='index'),
    path('content/',views.contect,name='contect'),
    path('about/',views.about,name='about'),
    path('singup/',views.singup,name='singup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('forget-password/',views.forget_password,name='forget-password'),
    path('Verify-otp/',views.Verify_otp,name='Verify-otp'),
    path('new-password/',views.new_password,name='new-password'),
    path('change-password/',views.change_password,name='change-password'),
    path('add-product/',views.add_product,name='add-product'),
    path('add-sub-details/',views.add_sub_details,name='add-sub-details'),
    path('view-product/',views.view_product,name='view-product'),
    path('edit-product/<int:pk>/',views.edit_product,name='edit-product'),
]
