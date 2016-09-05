from django.shortcuts import render
import os
# Create your views here.

## This fucntion gets the directories name and and resturns a filtered list
def listdir_except(path, avoid):
    for f in os.listdir(path):
        for l in avoid:
            if l in f:
                break
            else:
               yield f
               break


def sloppycell_reports_front(request):
    dir_list = listdir_except('sloppycellreports/static/sloppycellreports',avoid=['.DS','populate'])
    return render(request, 'sloppycellreports/scr_front.html',{'dir_list' : dir_list})

def sloppycell_reports_display_current_fitting(request,fitting_folder="current_fitting"):
    networks = listdir_except('sloppycellreports/static/sloppycellreports/'+fitting_folder+'_sloppyCell/images/',avoid=['.png'])
    dir_list = os.listdir('sloppycellreports/static/sloppycellreports/'+fitting_folder+'_sloppyCell/images/')
    constraints =[]
    for file_item in dir_list:
        if 'constraint' in file_item:
            constraints.append(file_item)
        elif 'cost' in file_item:
            cost = file_item 
    return render(request, 'sloppycellreports/scr_current_fitting.html',{'networks':networks,'fitting_folder': fitting_folder,'constraints': constraints, 'cost': cost})


def sloppycell_reports_display_current_fitting_network(request,fitting_folder="current_fitting",network=0):
    networks = listdir_except('sloppycellreports/static/sloppycellreports/'+fitting_folder+'_sloppyCell/images/',avoid=['.png'])
    network_plots = os.listdir('sloppycellreports/static/sloppycellreports/'+fitting_folder+'_sloppyCell/images/'+network)
    dir_list = os.listdir('sloppycellreports/static/sloppycellreports/'+fitting_folder+'_sloppyCell/images/')
    constraints =[]
    for file_item in dir_list:
        if 'constraint' in file_item:
            constraints.append(file_item)
        elif 'cost' in file_item:
            cost = file_item 
    return render(request, 'sloppycellreports/scr_network.html',{'networks':networks,'network':network , 'network_plots': network_plots,
            'fitting_folder': fitting_folder,'constraints': constraints, 'cost': cost})



def sloppycell_reports_display_notebook(request,notebook_folder="020916"):

    return render(request, 'sloppycellreports/notebook/'+notebook_folder+'_sloppyCell/html/fitting_'+notebook_folder+'.html')