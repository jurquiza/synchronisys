from django.conf.urls import  include,url
from . import views

urlpatterns = [
        url(r'^$', views.sloppycell_reports_front, name='sloppycell_reports_front'),
	url(r'scr_current_fitting/$', views.sloppycell_reports_display_current_fitting, name= "sloppycell_reports_display_current_fitting")
]
