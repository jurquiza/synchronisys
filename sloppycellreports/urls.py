from django.conf.urls import  include,url
from . import views

urlpatterns = [
        url(r'^$', views.sloppycell_reports_front),
        url(r'scr_current_fitting/$', views.sloppycell_reports_display_current_fitting),
        url(r'scr_current_fitting/(?P<fitting_folder>[0-9]{6})_sloppyCell$', views.sloppycell_reports_display_current_fitting),
        url(r'scr_current_fitting/(?P<fitting_folder>[0-9]{6})_sloppyCell/network/(?P<network>.*)$', views.sloppycell_reports_display_current_fitting_network),
        url(r'notebook/(?P<notebook_folder>[0-9]{6})$', views.sloppycell_reports_display_notebook),
]
