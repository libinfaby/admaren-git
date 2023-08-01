import requests
from getpass import getpass

from token_obtain import generate_new_token


username = input("Enter username: ")
password = getpass("Enter password: ")

access_token = generate_new_token(username, password)

auth_headers = {
    'Authorization': f'Bearer {access_token}',
} 

overview_endpoint = "http://localhost:8000/api/snippet/overview/"
overview_response = requests.get(overview_endpoint, headers=auth_headers)    

print(overview_response.json())
