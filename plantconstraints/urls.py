from django.conf.urls import  include,url
from . import views

urlpatterns = [
	url(r'', views.plantconstraints_front, name='views.plantconstraints_front'),

]
