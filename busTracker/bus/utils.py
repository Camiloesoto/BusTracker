import requests
import urllib


def aproximated_time(origin, destination):
    api_url = "https://www.mapquestapi.com/directions/v2/route?"
    key = "ISzleJZDHOyHT1k9p7jpI87YTGDUWHvT"
    url = api_url + urllib.parse.urlencode({"key": key, "from": origin, "to": destination})
    json_data = requests.get(url).json()

    return json_data['route']['legs'][0]["formattedTime"]
