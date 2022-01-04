import requests
import json

from requests.api import request


URL="http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    data=r.json()
    print(data)

# get_data(2)


def post_data():
    data={
        'name': 'Sajid', 'roll': 104, 'city': 'Chembure'
    }
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)

# post_data()

def update_data():
    data={
        'id':4,'name': 'Rohit', 'roll': 105, 'city': 'kurla'
    }
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    data=r.json()
    print(data)

# update_data()

def delete_data():
    data={
        'id':4
    }
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    data=r.json()
    print(data)

delete_data()