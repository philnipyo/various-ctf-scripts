# Notes
# Encoded 15 times!
# 5 times encoded using base 64
# 5 times encoded using base 32
# 5 times encoded using base 16

# Import the necessary base64 library
from base64 import *

# Initialize the variable to use the selected file
rawFlag = open("encodedflag.txt", "r")

# Get and set the first and only line of the file.
# The retrieved line is a string.
target = rawFlag.readline()

# Loop 5 times decoding the line using base16
for i in range(1, 6):
    target = b16decode(target)

# Loop 5 times dcoding the line using base32
for i in range(1, 6):
    target = b32decode(target)

# Loop 5 times dcoding the line using base64
for i in range(1, 6):
    target = b64decode(target)

print(target)
