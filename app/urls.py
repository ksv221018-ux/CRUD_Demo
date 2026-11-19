from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('insert/', insert_data, name='insert'),
    path('show/', read_data, name='read'),
    path('update/<int:id>/', update_data, name='update'),
    path('delete/<int:id>/', delete_data, name='delete'),
    path('logout/', user_logout, name='logout'),
]