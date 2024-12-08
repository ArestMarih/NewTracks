import requests

def joinGecko():
    url = "https://api.coingecko.com/api/v3/ping?x_cg_demo_api_key=CG-r1umQzviBjg5aMeDfVcjvbjr"
    resp = requests.get(url)
    return print(resp)

joinGecko()