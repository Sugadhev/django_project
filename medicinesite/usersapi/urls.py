from django.urls import path
from . import views

urlpatterns = [
    # its for the  response
    path('simpleapi', views.simpleapi, name='simple_api'),
    path('login', views.login, name='login_api'),
    path('medicinedetails',views.medicinedetails,name='medicinedetails_name_api'),

    path("create/", views.CreateTodoAPIView.as_view(),name="todo_create"),
    path("update/<int:pk>/",views.UpdateTodoAPIView.as_view(),name="update_todo"),
    path("delete/<int:pk>/",views.DeleteTodoAPIView.as_view(),name="delete_todo")
]

