#!/usr/bin/env python

with open('input') as file:
    instructions=file.read()

up = instructions.count('(')
down = instructions.count(')')

print(f'{up-down}')
