from django.shortcuts import render
from . import utils

def home(request):
    origen = request.GET.get('origen')
    destination = request.GET.get('destination')
    time = utils.aproximated_time(origen, destination)
    return render(request, 'home.html', {'time': time})
