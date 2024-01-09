import math
#ok so what i want to do is create a dictionary that goes from seed to location - this might be needlessly complex but it's COOL OK
#new idea the first one is cool but i wanna see if i can just "move" the seed number by checking if it's within two numbers instead
#of having a thing for every number

#seeds, soil, fertilizer, water, light, temperature, humidity, location = 
def part1():
    closest = math.inf
    lists = open('input.txt').read().split("\n\n")
    seeds = lists.pop(0).split(":")[1].strip().split(" ")
    for seed in seeds:
        source = int(seed)
        for list in lists:
            #all the ranges 
            for value_set in list.split("\n")[1:]:
                #destination, source, length
                dest_start, source_start, length = [int(value) for value in value_set.split(" ")]
                if source >= source_start and source <= (source_start + length):
                    source = source - source_start + dest_start
                    break
            
        closest = min(source, closest)
    print(closest)

part1()