import re

data = [line for line in open('input.txt').readlines()]
#Locations in x, y form (so need to reverse to search list)
numLocations = [[] for i in range(len(data))]
numbers = [[] for i in range(len(data))]
symbolLocations = []

def grabInfo():
    #edge case for last number
    data[len(data)-1] += '\n'
    numLength = 0
    for i, line in enumerate(data):
        numLength = 0
        for j, point in enumerate(line):
            if re.match('\d', point):
                numLength += 1
            elif numLength > 0:
                locList = []
                for n in range(numLength):
                    locList.append(j-n-1)
                numLocations[i].append(locList)
                #The composite number from the components
                numbers[i].append(int(data[i][j-numLength:j]))
                numLength = 0
            if point != '.' and point != '\n' and re.match('\d', point) == None:
                symbolLocations.append((j, i))
grabInfo()
def part1():
    sum = 0
    for location in symbolLocations:
        x, y = location
        popSet = set()
        for a in [-1, 0, 1]:
            for b in [-1, 0, 1]:
                #if y+b is in the bounds of the lists
                if y+b >= 0 and y+b < len(numLocations) and len(numLocations[y+b]) > 0:
                    #see if there's a corresponding location
                    for i, numSet in enumerate(numLocations[y+b]):
                        if x+a in numSet:
                            #append the *list* location of coords that correspond to the number found
                            popSet.add((y+b, i))
                #prevent doublecounts by removing used numbers
                while len(popSet) > 0:
                    popPosition = popSet.pop()
                    sum += numbers[popPosition[0]].pop(popPosition[1])
                    numLocations[popPosition[0]].pop(popPosition[1]) 
    print(sum)
def part2():
    sum = 0
    for location in symbolLocations:
        x, y = location
        popSet = set()
        for a in [-1, 0, 1]:
            for b in [-1, 0, 1]:
                #if y+b is in the bounds of the lists
                if y+b >= 0 and y+b < len(numLocations) and len(numLocations[y+b]) > 0:
                    #see if there's a corresponding location
                    for i, numSet in enumerate(numLocations[y+b]):
                        if x+a in numSet:
                            #append the *list* location of coords that correspond to the number found
                            popSet.add((y+b, i))
        #yeah we poppin
        if len(popSet) == 2:
            y1, numpos1 = popSet.pop()
            
            y2, numpos2 = popSet.pop()

            sum += numbers[y1][numpos1]*numbers[y2][numpos2]
    print(sum)
part2()