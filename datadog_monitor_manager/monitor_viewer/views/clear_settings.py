from django.shortcuts import render, redirect
from django.http import HttpResponse
from monitor_viewer.services.datadog_client import DatadogClient

def clear(request):
    # return HttpResponse('リスト')
    request.session.clear()
    # return render(request, 'monitor_list.html', {})
    return redirect('/monitor_viewer/monitor/')