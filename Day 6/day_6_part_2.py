import os
import numpy as np
from pandas.core.indexes import period


def read_in_file(filepath):
    f = open(filepath, "r")
    content = f.readlines()
    return content

def main(period_len):
    filepath = r"day_6_puzzle_input.txt"
    data = read_in_file(filepath)

    #parse data
    fish_starting_timers = np.array([int(fish_starting_timer) for fish_starting_timer in data[0].split(",")])
    #transform into fish counts
    unique, counts = np.unique(fish_starting_timers, return_counts=True)

    max_pond_size = 8
    starting_pond = np.zeros(max_pond_size+1)
    ponds = []
    #populate starting pond
    for idx in range(len(unique)):
        #idx = internal timer
        #value = num fish at that internal timer
        timer = unique[idx]
        fish_count = counts[idx]
        starting_pond[timer] = fish_count
    ponds.append(starting_pond) 

    #model growth
    fish_reset_timer = 0
    fish_reset_to = 6
    for day_num in range(1,period_len+1):
        prev_pond = ponds[day_num-1]
        
        #age fish that need to be age
        current_pond = np.zeros(max_pond_size+1)
        #fill current pond with aged fish
        current_pond[:-1] = prev_pond[1:]

        #reset fish
        num_fish_reset = prev_pond[fish_reset_timer]
        current_pond[-1] = num_fish_reset
        current_pond[fish_reset_to] += num_fish_reset

        ponds.append(current_pond)

        print(sum(current_pond), day_num)




main(256)