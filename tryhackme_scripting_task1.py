# File is base64 encoded 50 times

from base64 import *

file = open("b64.txt")

# Retrieve and store sole line into variable
text = file.readline()

for i in range(1, 51):
	# Loop through and decode text's string contents using b64
	text = b64decode(text)

# Final result is HackBack2019=
print(text)