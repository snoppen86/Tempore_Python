import requests

URL = f"http://api.sl.se/api2/trafficsituation.json?key=4d45370ae02145a89811b056da8ad1f2"


def get_travel_status():
    r = requests.get(url=URL)
    return r.json()

