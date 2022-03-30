# Test the rest api
import requests


def test():
    c = requests.get("http://localhost:5000/add/hello")
    if c.status_code == 200:
        print("Success adding")
    else:
        print("Error:", c.json()["Error"])
    c = requests.get("http://localhost:5000/search/hello")
    if c.json()["Status"] == True:
        print("Success searching")
    else:
        print("not found")
    c = requests.get("http://localhost:5000/suggest/he")
    if not c.json()["Status"] == []:
        print("Success suggesting")
    else:
        print("Error:", c.json()["Error"])
    c = requests.get("http://localhost:5000/struct")
    if c.status_code == 200:
        print("Success struct")
    else:
        print("Error:", c.json()["Error"])
    requests.get("http://localhost:5000/add/hello")
    c = requests.get("http://localhost:5000/remove/hello")
    if c.status_code == 200:
        print("Success removing")
    else:
        print("Error:", c.json()["Error"])


test()
