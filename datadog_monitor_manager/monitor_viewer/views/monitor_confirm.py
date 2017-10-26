from django.shortcuts import render
from django.http import HttpResponse
from monitor_viewer.services.datadog_client import DatadogClient
import os

def confirm(request):
    print(str(request.POST)) 
    body = request.POST
    print(body.get('msg'))
    monitor = {}
    monitor['text'] = body.get('msg')
    return render(request, 'monitor_confirm.html',{ "monitor": monitor })