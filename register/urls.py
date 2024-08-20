from django.urls import path
from . import views

urlpatterns=[
    path("",views.firstp,name="firstpage"),
    path("register/<int:user_id>",views.user_detail,name='userspage'),    
]