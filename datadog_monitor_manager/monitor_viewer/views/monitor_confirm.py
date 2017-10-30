from django.shortcuts import render
from django.http import HttpResponse
import json

def confirm(request):
    body = request.POST
    print(body.get('msg'))
    monitor = {}
    monitor['text'] = body.get('msg')
    monitor['name'] = json.loads(body.get('msg')).get('name')
    return render(request, 'monitor_confirm.html',{ "monitor": monitor })