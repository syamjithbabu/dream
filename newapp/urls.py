from django.urls import path
from . import views

app_name="newapp"

urlpatterns = [
   # path('',views.New,name='new'),
   path('Hi/',views.Good,name='hello'),
   path('Dark/',views.Dark,name='dark'),
   path('Class/',views.Class,name='new'),
   path('',views.New,name='class'),
   
]