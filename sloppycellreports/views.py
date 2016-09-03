from django.shortcuts import render
import os
# Create your views here.

def sloppycell_reports_front(request):
	return render(request, 'sloppycellreports/scr_front.html',{})

def sloppycell_reports_display_current_fitting(request):
	return render(request, 'sloppycellreports/scr_current_fitting.html',{})
