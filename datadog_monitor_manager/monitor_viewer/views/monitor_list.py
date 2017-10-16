from django.shortcuts import render
from django.http import HttpResponse
from monitor_viewer.services.datadog_client import DatadogClient
import os

def get_list(request):
    # return HttpResponse('リスト')
    client = DatadogClient(api_key=os.getenv('DD_API_KEY'),app_key=os.getenv('DD_APP_KEY'))
    monitors = client.get_monitors()

    return render(request, 'monitor_list.html',{'monitors': monitors})