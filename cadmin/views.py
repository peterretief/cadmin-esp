from django.shortcuts import render
from django.utils import timezone
from .models import Request

def print_test(request):
    requests = Request.objects.first()
    return render(request, 'cadmin/request_print.html', {'requests': requests})

def connect_mqtt():
    print("hello")	

def request_list(request):
  #  requests = Request.objects.all()
  #  requests = Request.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    requests = Request.objects.filter(status=4)
    return render(request, 'cadmin/request_list.html', {'requests': requests})
