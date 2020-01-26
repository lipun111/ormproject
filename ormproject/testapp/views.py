from django.shortcuts import render
from django.db.models import Q
from django.db.models import Avg,Sum,Min,Max,Count
from .models import Employee

# Create your views here.

def home_view(request):
    emp=Employee.objects.all()
    return render(request, 'testapp/home.html',{'emp':emp})

def aggregate_view(request):
    avg=Employee.objects.all().aggregate(Avg('esal'))
    max=Employee.objects.all().aggregate(Max('esal'))
    min=Employee.objects.all().aggregate(Min('esal'))
    sum=Employee.objects.all().aggregate(Sum('esal'))
    count=Employee.objects.all().aggregate(Count('esal'))
    my_dict={"avg":avg, "max":max, "min":min, "count":count, "sum":sum}
    return render(request, 'testapp/aggregate.html', my_dict) 

#keys= my_dict.keys(), values=my_dict.get(my_dict.keys())
