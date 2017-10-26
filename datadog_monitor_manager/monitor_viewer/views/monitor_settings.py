from django.shortcuts import render
from django.http import HttpResponse

def get_settings(request):
    # return HttpResponse('リスト')
    return render(request, 'monitor_settings.html', {})