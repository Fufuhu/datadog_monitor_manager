from django.conf.urls import url
from monitor_viewer.views import monitor_list

urlpatterns = [
    url(r'^monitor/$', monitor_list.get_list, name='monitor_list'),
]