import re

data = open('input.txt').readlines()
def part1():
    totals = {'red': 12, 'green': 13, 'blue': 14}
    sum = 0
    pattern = "(\d [a-z]+)+"
    for i, line in enumerate(data):
        for cubes in re.findall(pattern, line):
            
part1()