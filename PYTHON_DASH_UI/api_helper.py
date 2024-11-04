import requests
import json

def call_api(path, method, body=None):
    API_HOST = "http://127.0.0.1:8080"
    url = API_HOST + path
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}

    try:
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            response = requests.post(url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent="\t"))
        elif method == 'PUT':
            response = requests.put(url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent="\t"))
        elif method == 'DELETE':
            response = requests.delete(url, headers=headers)
        else:
            print("Unsupported HTTP method:", method)
            return
        return response
    except Exception as ex:
        print(ex)
