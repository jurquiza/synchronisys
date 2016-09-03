from django.shortcuts import render
import os
# Create your views here.

def sloppycell_reports_front(request):
    dir_list = os.listdir('static/')
    return render(request, 'sloppycellreports/scr_front.html',{'dir_list' : dir_list})

def sloppycell_reports_display_current_fitting(request):
    dir_list = os.listdir('static/')
    cost = os.listdir('static/mock1')
    return render(request, 'sloppycellreports/scr_current_fitting.html',{'constraints': dir_list, 'cost' : cost})
