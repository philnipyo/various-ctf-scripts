import requests 

# Define the URL to send+retrieve requests
u = 'http://TRYHACKME_MACHINE_IP/api/'

for i in range(1, 100, 2):
    # Append string version of i to the URL
    URL = u + str(i)
    r = requests.get(url = URL)
    # Decode the JSON into string data
    data = r.json()
    # Prints out information in the following format: Number | Result
    print('Item number {} yields: {}').format(data['item_id'], data['q'])
