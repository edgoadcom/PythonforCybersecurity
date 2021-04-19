import requests

url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces"   # using ietf-interfaces
url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/Cisco-IOS-XE-native:native/interface" # reporting all interfaces
url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback=100" # reporting just loopback 100


payload={}
headers = {
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU='
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)
