# Notes: Encoded 15 times:
# 5 times encoded using base 64
# 5 times encoded using base 32
# 5 times encoded using base 16
# Reverse the decoding order (16->32->64 instead of 64->32->16)

# Import the necessary base64 library
from base64 import *

# Initialize the variable to use the selected file
rawFlag = open("encodedflag.txt", "r")

# Get and set the first and only line of the file.
# The retrieved line is a string.
target = rawFlag.readline()


for i in range(1, 16):
    # Loop 5 times decoding the line using base16
    if i >= 1 and i < 6:
        target = b16decode(target)
    # Loop 5 times dcoding the line using base32
    elif i >=6 and i < 11:
        target = b32decode(target)
    # Loop 5 times dcoding the line using base64
    elif i >= 11 and i < 16:
        target = b64decode(target)
else:
    print(target)
