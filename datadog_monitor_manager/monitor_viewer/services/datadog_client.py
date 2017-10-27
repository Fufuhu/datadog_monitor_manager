from datadog import initialize, api
import json

class DatadogClient():
    def __init__(self, api_key, app_key, **kwargs):
        self.__options = {
            'api_key': api_key,
            'app_key': app_key,
        }
        initialize(**self.__options)
    
    def get_monitors(self):
        return api.Monitor.get_all()  

    def get_monitor(self, monitor_id):
        return api.Monitor.get(id=monitor_id)

    def update_monitor(self, monitor_id, message):
        json_body = json.loads(message)
        query = json_body.get('query')
        name = json_body.get('name')
        msg = json_body.get('message')
        options = json_body.get('options')
        tags = json_body.get('tags')


        api.Monitor.update(id=monitor_id, query=query, name=name, message=msg, options=options, tags=tags)