from django.shortcuts import render, redirect
from django.http import HttpResponse
from monitor_viewer.services.datadog_client import DatadogClient

def get_list(request):
    # return HttpResponse('リスト')
    if 'app_key' not in request.session or 'api_key' not in request.session:
        return render(request, 'monitor_settings.html', {})
    client = DatadogClient(api_key=request.session.get('api_key'),
                           app_key=request.session.get('app_key'))
    monitors = client.get_monitors()

    if 'errors' in monitors:
        param = {
            'is_error': True,
        }
        return render(request, 'monitor_settings.html', {'param': param})

    return render(request, 'monitor_list.html',{'monitors': monitors})