from django.contrib import admin
from django.urls import path, include
from users import views




urlpatterns = [
    # its for login&logout
    path('admin/', admin.site.urls),
    path('', include('users.urls')),

    # crud application
    # insert button
    path('insert/', views.insert),

    # home
    path('', views.home, name="Home"),

    # update
    path('update/<int:id>', views.update,),

    # delete
    path('delete/<int:id>', views.delete,),
     
    # api 
    path('usersapi/', include('usersapi.urls')),

]
