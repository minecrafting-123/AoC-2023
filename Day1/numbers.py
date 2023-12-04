import re
def part1():
    sum = 0
    regex = "[0-9]"
    for line in open('input.txt').readlines():
        nums = re.findall(regex, line)
        sum += int(nums[0]) * 10 + int(nums[-1])
    print(sum)
part1()
#There was something with re.findall() that made it not work... i think it was a issue with overlapping letters like nineight wouldn't be (9, 8)
def part2():
    sum = 0
    # numbers = {'one': 1, '1': 1, 'two': 2, '2': 2, 'three': 3, '3': 3, 'four': 4, '4': 4, 'five': 5, '5': 5, 'six': 6, '6': 6, 'seven': 7, '7': 7, 'eight': 8, '8': 8, 'nine': 9, '9': 9}
    # pattern = re.compile('|'.join(numbers))
    regex = "[0-9]"
    for line in open('input.txt').readlines():
        newline = line.replace('one', 'o1e').replace('two', 't2o').replace('three', 't3e').replace('four', 'f4r').replace('five', 'f5e').replace('six', 's6x').replace('seven', 's7n').replace('eight', 'e8t').replace('nine', 'n9e')
        #found = re.findall(pattern, line)
        #print(line, found, sum)
        nums = re.findall(regex, newline)
        sum += int(nums[0]) * 10 + int(nums[-1])
    print(sum)

part2()