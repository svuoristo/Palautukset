import requests

request_joke = 'https://api.chucknorris.io/jokes/random'

try:
    answer = requests.get(request_joke)
    if answer.status_code == 200:
        json_answer = answer.json()
        print(json_answer["value"])
except requests.exceptions.RequestException:
    print("The search could not be performed.")