from django.shortcuts import render

def request_list(request):
    return render(request, 'cadmin/request_list.html', {})

# Create your views here.
