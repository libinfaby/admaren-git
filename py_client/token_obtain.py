import requests


def generate_new_token(username, password):
    auth_endpoint = "http://localhost:8000/api/token/"
    data = {
        "username": username,
        "password": password,
    }
    auth_response = requests.post(auth_endpoint, json=data)

    try:
        access_token = auth_response.json()['access']  
        return access_token
    except KeyError as err:
        print(err)