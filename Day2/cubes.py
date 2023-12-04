import re

data = open('input.txt').readlines()
def part1():
    totals = {'red': 12, 'green': 13, 'blue': 14}
    sum = 0
    pattern = "(\d+ [a-z]+)+"
    for i, line in enumerate(data):
        possible = True
        for cubes in re.findall(pattern, line):
            number, color = cubes.split(' ')
            if int(number) > totals[color]:
                possible = False
        if possible:
            sum += i + 1
    print(sum)
def part2():
    sum = 0
    pattern = "(\d+ [a-z]+)+"
    for line in data:
        product = 1
        minNeeded = {'red': 0, 'green': 0, 'blue': 0}
        for cubes in re.findall(pattern, line):
            number, color = cubes.split(' ')
            if int(number) > minNeeded[color]:
                minNeeded.update({color: int(number)})
        for values in minNeeded.values():
            product *= values
        sum += product
    print(sum)
            
part2()