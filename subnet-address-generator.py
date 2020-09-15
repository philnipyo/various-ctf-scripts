import random

# Define address to be appended with generated integers
address = ''

# Generate a random integer
def genInt():
    return str(random.randint(1, 255))

# Generate an appropriate subnet mask number
def genMask():
    return ' /' + str(random.randint(1, 32))

for i in range(4):
    # First three octets get an integer followed by a period
    if i != 3:
        address += genInt() + '.'
    # Last octet of address does not get a period
    else:
        address += genInt()

# Append complete IPv4 address with a subnet mask
address += genMask()
print(address)
