import requests
import json

base_url = 'https://api.meraki.com/api/v1'
key = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
org_id = '681155'

def get_dev():
    url = base_url + f"/organizations/{org_id}/inventory/devices"
    headers = {
        "X-Cisco-Meraki-API-Key": key
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    print(json.dumps(data,indent=4))
    count=0
    num=len(data)
    for i in range(num):
        id_network = data[i]['networkId']
        if (id_network == None):
            count += 1
            result = data[i]
            print(json.dumps(result, indent=4))
        print('devices network id is null', count)

get_dev()