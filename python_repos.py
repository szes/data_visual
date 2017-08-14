import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"

try:
    r = requests.get(url)
    print("Status code:", r.status_code)

    response_dict = r.json()

    print(response_dict.keys())
except:
    print("Get url error!")