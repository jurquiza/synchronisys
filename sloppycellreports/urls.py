from django.conf.urls import  include,url
from . import views

urlpatterns = [
        url(r'^$', views.sloppycell_reports_front),
        url(r'scr_current_fitting/$', views.sloppycell_reports_display_current_fitting),
        url(r'scr_current_fitting/(?P<fitting_folder>[0-9]{6})$', views.sloppycell_reports_display_current_fitting),
]
