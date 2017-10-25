from django.conf.urls import url
from monitor_viewer.views import monitor_list, monitor_detail

urlpatterns = [
    url(r'^monitor/$', monitor_list.get_list, name='monitor_list'),
    url(r'^monitor/(?P<monitor_id>\d+)/$', monitor_detail.get_detail, name='monitor_detail'),
]