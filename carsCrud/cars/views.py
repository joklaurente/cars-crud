from django.shortcuts import render
from .models import Car
from .forms import CarForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect

def list_car(request):
    car_list = Car.objects.all()
    context = {
        'car_list': car_list,
    }
    return render(request, "cars/list.html", context)

def update_car(request, id): 
    # context ={} 
    # context["data"] = Car.objects.get(id = id) 
    # return render(request, "cars/details.html", context)
    context ={} 
    obj = get_object_or_404(Car, id = id) 
    form = CarForm(request.POST or None, instance = obj) 
    if form.is_valid(): 
        form.save() 
        return redirect('list_car') 
    context = {
        "form": form,
        "car_id": id
    }
    return render(request, "cars/update.html", context) 

def create_car(request): 
    
    context ={} 
    form = CarForm(request.POST or None) 
    if form.is_valid(): 
        form.save() 
        return redirect('list_car')
    context = {
        'form': form,
    }
    return render(request, "cars/create.html", context)

def delete_car(request, id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # fetch the object related to passed id 
    obj = get_object_or_404(Car, id = id) 
  
  
    if request.method =="POST": 
        obj.delete() 
        return redirect('list_car') 
    return render(request, "cars/delete.html", context)