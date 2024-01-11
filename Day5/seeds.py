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

def process(map, og_start, og_end):
    new_ranges = []
    answer_ranges = []
    for value_set in map.split("\n")[1:]:
        dest_start, source_start, length = [int(value) for value in value_set.split(" ")]
        print("dest_start, source_start, length: ", dest_start, source_start, length)
        new_ranges.append((og_start, og_end, dest_start))
        for seed_range in new_ranges:
            seed_start, seed_end, _ = seed_range
            print("seed_start, seed_end: ", seed_start, seed_end)
            #if start of mapping is in the middle of the values
            if source_start >= seed_start and source_start <= seed_end:
                #check if ending of range is within beeg range, if not
                if source_start + length > seed_end:
                    new_ranges.remove(seed_range)
                    new_ranges.append((seed_start, source_start-1, dest_start))
                    new_ranges.append((source_start, seed_end, dest_start + source_start - seed_start))
                #if ending of range is within beeg range
                else: 

            #if start of source is in the middle of mapping
    for new_range in new_ranges:
        start, end, mapped_start = new_range
        answer_ranges.append((mapped_start, mapped_start + end-start))
    print(answer_ranges)
    return answer_ranges



def part2():
    closest = math.inf
    lists = open('test.txt').read().split("\n\n")
    seeds = lists.pop(0).split(":")[1].strip().split(" ")
    for i in range(0, len(seeds), 2):
        initial, length = int(seeds[i]), int(seeds[i+1])
        for list in lists:
            process(list, initial, initial+length)
            exit()
        #all the ranges 
        
        closest = min(source, closest)
        print(closest)
        exit()
    print(closest)
part2()