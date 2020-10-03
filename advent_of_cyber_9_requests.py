# 10.10.169.100 @ port 3000
# Receieve {"value":"s","next":"f"} when accessing "/"
# The JSON object retrieved will need to be converted from unicode to ASCII(as shown in the supporting material)
# All the values retrieved until the 'end' will be the flag(end is not included in the flag)

import requests

final = '123456'
next = ''

path = '/'
host = 'http://10.10.169.100:3000'

while(next != 'end'):
    # Create response variable to store requests.get's results
    response = requests.get(host + path)
    print(response)
    # status_code = response.status_code
    # print(status_code)
    # Retrieve JSON object from host + path
    json_response = response.json()
    print(json_response)
    # Convert JSON object from unicode to ASCII
    # json_response needs to be converted to str?
    converted_response = str(json_response).encode('ascii')
    print(converted_response)
    text = response.text
    print(text.next)
    print()


# print(next)



# Append value key's value to value
# Change the path variable's value to the next key value
