from django.shortcuts import render, redirect
from django.http import HttpResponse
from monitor_viewer.services.datadog_client import DatadogClient

def save(request):
    # return HttpResponse('リスト')
    request.session['api_key'] = request.POST.get('api_key')
    request.session['app_key'] = request.POST.get('app_key')
    print(request.session['api_key'])
    print(request.session['app_key'])
    client = DatadogClient(api_key=request.session.get('api_key'),app_key=request.session.get('app_key'))
    monitors = client.get_monitors()

    return redirect('/monitor_viewer/monitor/')
    # return render(request, 'monitor_list.html', {"monitors": monitors})