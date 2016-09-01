from django.shortcuts import render

# Create your views here.
def plantconstraints_front(request):
        return render(request, 'plantconstraints/plantconstraints_front.html',{})
