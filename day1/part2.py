#!/usr/bin/env python

with open('input') as file:
    instructions=file.read()

floor = 0
for index, value in enumerate(instructions):
    if value=='(':
        floor = floor + 1
    else:
        floor = floor -1

    if floor == -1:
        print(f'entering basement at instruction {index+1}')
        break
