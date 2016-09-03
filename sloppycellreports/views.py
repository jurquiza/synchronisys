from django.shortcuts import render
import os
# Create your views here.

def sloppycell_reports_front(request):
    dir_list = os.listdir('static/')
    return render(request, 'sloppycellreports/scr_front.html',{'dir_list' : dir_list})

def sloppycell_reports_display_current_fitting(request,fitting_folder="current_fitting"):
    dir_list = os.listdir('sloppycellreports/static/sloppycellreports/'+fitting_folder+'/images/')
    constraints =[]
    for file_item in dir_list:
        if 'constraint' in file_item:
            constraints.append(file_item)
        elif 'cost' in file_item:
            cost = file_item 
    return render(request, 'sloppycellreports/scr_current_fitting.html',{'fitting_folder': fitting_folder,'constraints': constraints, 'cost': cost})
