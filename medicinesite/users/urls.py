from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    
    # login &logout
    path('', views.home, name='home'), 
    path('profile/', views.profile, name='profile'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    # crud
    path('', views.userregisteration, name='userregisteration'),
    path('register/', views.register, name='register'),
    # about
    path('about/',views.about,name='about'),
    # contact
    path('contact/',views.contact,name="contact")
]
   


