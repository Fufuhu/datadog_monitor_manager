from django.shortcuts import render
from django.http import HttpResponse
from monitor_viewer.services.datadog_client import DatadogClient
import os
import json

def get_detail(request,monitor_id=None):
    # return HttpResponse('リスト')
    client = DatadogClient(api_key=os.getenv('DD_API_KEY'),app_key=os.getenv('DD_APP_KEY'))
    monitor = client.get_monitor(monitor_id=monitor_id)
    dumped_monitor = json.dumps(monitor, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '))

    return render(request, 'monitor_detail.html',{ 'monitor': monitor, 'text': dumped_monitor})