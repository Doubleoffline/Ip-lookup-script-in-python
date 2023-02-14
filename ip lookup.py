import requests
import json

ip_address = input("Enter an IP address: ")

url = f"http://ip-api.com/json/{ip_address}"
response = requests.get(url)
data = json.loads(response.text)

print(f"IP address: {data['query']}")
print(f"City: {data['city']}")
print(f"Region: {data['regionName']}")
print(f"Country: {data['country']}")
print(f"ISP: {data['isp']}")

input("Press any key to close...")
