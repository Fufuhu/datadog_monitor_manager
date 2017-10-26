from django.conf.urls import url
from monitor_viewer.views import monitor_list, monitor_detail, monitor_settings, monitor_save

urlpatterns = [
    url(r'^monitor/$', monitor_list.get_list, name='monitor_list'),
    url(r'^monitor/save/$', monitor_save.save, name='monitor_save'),
    url(r'^monitor/settings/$', monitor_settings.get_settings, name='monitor_settings'),
    url(r'^monitor/(?P<monitor_id>\d+)/$', monitor_detail.get_detail, name='monitor_detail'),
]