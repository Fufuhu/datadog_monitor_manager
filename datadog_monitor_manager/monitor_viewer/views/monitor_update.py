from django.shortcuts import redirect
from django.http import HttpResponse
import os
import json
from monitor_viewer.services.datadog_client import DatadogClient

def update(request):
    print(str(request.POST))
    body = request.POST
    print(body.get('msg'))
    message = body.get('msg')
    monitor_id = json.loads(message).get('id')

    client = DatadogClient(api_key=request.session.get('api_key'),
                           app_key=request.session.get('app_key'))
    client.update_monitor(monitor_id=monitor_id, message=message)

    return redirect('/monitor_viewer/monitor/')
