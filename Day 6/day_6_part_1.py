import os
import numpy as np


def read_in_file(filepath):
    f = open(filepath, "r")
    content = f.readlines()
    return content

def main(period_len):
    filepath = r"day_6_test_input.txt"
    data = read_in_file(filepath)

    #parse data
    fish_starting_timers = np.array([int(fish_starting_timer) for fish_starting_timer in data[0].split(",")])

    #run model
    fish_pond = fish_starting_timers.copy() #contains all fish information
    reset_fish_state = 0
    for day in range(1,period_len+1):

        #check if any new laternfish are about to come
        fish_to_be_reset = fish_pond == 0
        fish_to_age = ~fish_to_be_reset
        #so age fish
        fish_pond[fish_to_age] -= 1
        if sum(fish_to_be_reset) > 0:
            #fish to be reset - internal goes to 6
            fish_pond[fish_to_be_reset] = 6
            #new fish gets a timer of 8
            num_fish_reset = len(fish_pond[fish_to_be_reset])
            new_fish = np.ones((num_fish_reset)) * 8
            fish_pond = np.append(fish_pond, new_fish)

        
        print("Day ", str(day) + " ", np.unique(fish_pond,return_counts=True), " ", len(fish_pond))
    

main(18)