import requests

url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces"

payload='''{
        "ietf-interfaces:interface": {
            "name": "Loopback100",
            "description": "Added with RESTCONF",
            "type": "iana-if-type:softwareLoopback",
            "enabled": true,
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": "172.16.100.1",
                        "netmask": "255.255.255.0"
                    }
                ]
            }
        }
    }'''
headers = {
  'Content-Type': 'application/yang-data+json',
  'Authorization': 'Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
