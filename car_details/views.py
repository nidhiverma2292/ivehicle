from django.shortcuts import render_to_response , get_object_or_404
from django.template import RequestContext
from models import Car
# Create your views here.
def index(request):

    cars = Car.objects.all()

    return render_to_response('index.html', locals(), context_instance = RequestContext(request))

def car_detail(request, id):
    car = get_object_or_404(id=id)

    return render_to_response('car.html', locals(), context_instance = RequestContext(request))
