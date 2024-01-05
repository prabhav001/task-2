from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.findtrains, name='find-train'), 
    path('alltrains/', views.index , name='viewtrains'), 
    path('result/',views.train_filter,name='train-filter')
    
]