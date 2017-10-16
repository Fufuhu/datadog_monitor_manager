from datadog import initialize, api


class DatadogClient():
    def __init__(self, api_key, app_key, **kwargs):
        self.__options = {
            'api_key': api_key,
            'app_key': app_key,
        }
        initialize(**self.__options)
    
    def get_monitors(self):
        return api.Monitor.get_all()  