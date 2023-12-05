import re
import math
data = [line.strip() for line in open('input.txt')]

def part1():
    sum = 0
    for line in data:
        pointValue = 1/2
        found = False
        winning, have = line.split('|')
        winningNums = re.findall('\d+', winning)
        #get rid of game num
        winningNums.pop(0)
        haveNums = re.findall('\d+', have)
        for num in winningNums:
            if num in haveNums:
                found = True
                pointValue *= 2
        if found:
            sum += pointValue
    print(sum)

part1()
def part2():
    copies = [1] * len(data)
    for i, line in enumerate(data):
        found = 0
        winning, have = line.split('|')
        winningNums = re.findall('\d+', winning)
        haveNums = re.findall('\d+', have)
        winningNums.pop(0)
        print(winningNums, haveNums)
        for num in winningNums:
            if num in haveNums:
                found += 1
        print(found)
        if found > 0:
            for j in range(found):
                copies[i+j+1] += 1 * copies[i]
        print(copies)
    print(sum(copies))
part2()

#test 9214963444 too high
