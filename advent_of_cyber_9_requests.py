# 10.10.169.100 @ port 3000
# Receieve {"value":"s","next":"f"} when accessing "/"
# The JSON object retrieved will need to be converted from unicode to ASCII(as shown in the supporting material)
# All the values retrieved until the 'end' will be the flag(end is not included in the flag)

import requests

# String to be printed after "end" is reached
flag = ''

path = '/'
host = 'http://10.10.169.100:3000'

while(next != 'end'):
    # Create response variable to store requests.get's results
    response = requests.get(host + path)

    # Retrieve JSON object from host + path
    json_response = response.json()

    # Initialize next and value variables to store the JSON object values as strings
    next = str(json_response["next"]).encode('ascii')
    value = str(json_response["value"]).encode('ascii')

    if next == 'end' or value == 'end':
        print('Flag is currently: {}'.format(flag))
        break
    else:
        print('Next path to take is: {}'.format(next))
        print('Value to be added is {}'.format(value))

        # Append value key's value to flag
        flag += value

        # Change the path variable's value to the next key value
        path = '/' + next

        print('Flag is currently: {}'.format(flag))
    
# Manually going through each link, the flag is sCrIPtKiDd