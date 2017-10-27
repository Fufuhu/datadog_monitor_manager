from django.conf.urls import url
from monitor_viewer.views import monitor_list, monitor_detail,\
 monitor_settings, monitor_confirm, monitor_settings_confirm,\
 clear_settings, monitor_update

urlpatterns = [
    url(r'^monitor/$', monitor_list.get_list, name='monitor_list'),
    url(r'^monitor/confirm/$', monitor_confirm.confirm, name='monitor_confirm'),
    url(r'^monitor/update/$', monitor_update.update, name='monitor_update'),
    url(r'^monitor/settings/$', monitor_settings.get_settings, name='monitor_settings'),
    url(r'^monitor/settings/clear/$', clear_settings.clear, name='clear_settings'),
    url(r'^monitor/settings/confirm/$', monitor_settings_confirm.save, name='monitor_settings_confirm'),
    url(r'^monitor/(?P<monitor_id>\d+)/$', monitor_detail.get_detail, name='monitor_detail'),
]