from django.shortcuts import render

# Create your views here.


from django.template.response import TemplateResponse
from Station.models import Reading


def home(request):
    data = Reading.objects.last()

    return TemplateResponse(request, 'index.html', {'data': data})
