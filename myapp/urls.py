from django.urls import path
from myapp.views import index,logout_view

app_name = 'myapp'

urlpatterns = [
    path('',index,name = 'index'),
    path('logout/',logout_view,name = 'logout'),
]