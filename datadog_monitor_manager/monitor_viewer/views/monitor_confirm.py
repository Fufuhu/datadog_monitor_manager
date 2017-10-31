from django.shortcuts import render
from django.http import HttpResponse
from monitor_viewer.services.datadog_client import DatadogClient
import json
import difflib
import re

def confirm(request):
    body = request.POST
    # print(body.get('msg'))
    monitor = {}
    monitor['text'] = body.get('msg')
    monitor['name'] = json.loads(body.get('msg')).get('name')

    # 既存モニター取得用のmonitor_idを取得
    json_body = json.loads(body.get('msg'))
    monitor_id = json_body.get('id')

    # api/app_keyを取得
    api_key = request.session.get('api_key')
    app_key = request.session.get('app_key')

    client = DatadogClient(api_key=api_key, app_key=app_key)

    monitor_result = client.get_monitor(monitor_id=monitor_id)
    monitor_setting_prev = json.dumps(monitor_result, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')).splitlines()
    monitor_setting_new = body.get('msg').splitlines()

    diff_result = difflib.ndiff(monitor_setting_prev, monitor_setting_new)
    monitor['diff'] = []

    line_number = 1
    for line in diff_result:
        line = line.replace(' ','&nbsp;')

        diff_line = {}
        diff_line['line'] = line
        if re.match(r"^\+.*", line):
            diff_line['is_add'] = True
        elif re.match(r"^\-.*", line):
            diff_line['is_add'] = False
        elif re.match(r"^\?.*", line):
            continue
        else:
            diff_line['is_add'] = None
        diff_line['line_number'] = line_number
        line_number = line_number + 1
        monitor['diff'].append(diff_line)
        

    return render(request, 'monitor_confirm.html', {"monitor": monitor})
