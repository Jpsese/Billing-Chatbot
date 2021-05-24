import json
import requests

def post_request(func):
    def wrapper(*args, **kw):
        print('@Teams: '+func.__name__)
        requestInfo = func(*args, **kw)

        messageUrl = requestInfo['url'] + requestInfo['convoId']+'/activities/'
        result = requests.post(
            messageUrl,
            json=requestInfo['payload']
        )
        if result:
            try:
                return result.json()
            except:
                pass
        return {}
    return wrapper

class TeamsOutputBuilder:

    def __init__(self, payload):
        self.payload = payload
        self.URL = payload