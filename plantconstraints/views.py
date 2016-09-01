from django.shortcuts import render
from .models import Parameter
# Create your views here.
def plantconstraints_front(request):
        return render(request, 'plantconstraints/plantconstraints_front.html',{})

def plantconstraints_display(request):
	parameters = Parameter.objects.all()
	return render(request, 'plantconstraints/plantconstraints_display.html', {'parameters': parameters})
