import requests

url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces/interface=Loopback100"

payload='''{
        "ietf-interfaces:interface": {
            "name": "Loopback100",
            "description": "Added with RESTCONF",
            "type": "iana-if-type:softwareLoopback",
            "enabled": true,
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": "172.16.100.11",
                        "netmask": "255.255.255.0"
                    }
                ]
            }
        }
    }'''
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json',
  'Authorization': 'Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU='
}

response = requests.request("PUT", url, headers=headers, data=payload, verify=False)

print(response.text)
