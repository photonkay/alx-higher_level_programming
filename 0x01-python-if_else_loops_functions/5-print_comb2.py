#!/usr/bin/python3

for number in range(0, 100):
    print("{:02}".format(number), end=",")
    if number == 99:
        print("{:02}".format(number))
