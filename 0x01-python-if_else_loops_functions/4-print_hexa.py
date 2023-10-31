#!/usr/bin/python3

for number in range(0, 99):
    hex = format(number, '0x')
    print("{} = 0x{}".format(number, hex))
