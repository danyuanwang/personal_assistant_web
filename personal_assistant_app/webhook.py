import requests
import json

def post_message(sender, message):
    url = "http://localhost:5005/webhooks/rest/webhook"
    r = requests.post(url, json={"sender": sender, "message": message})
    return json.loads(r.text)

#print(post_message("test", "hello"))