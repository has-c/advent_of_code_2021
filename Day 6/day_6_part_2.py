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

    #process
    unique, counts = np.unique(fish_starting_timers, return_counts=True)
    for 
    for stt
    print(d)
    #each element is a new fish pond
    # ponds = [fish_pond]
    

        # #age fish
        # for current_pond[]

        # #reset fish and create new fish
        # num_fish_reset = sum(fish_to_be_reset)
        # if num_fish_reset > 0:
        #     current_pond.loc[fish_to_be_reset, "fish_timer"] = 6
        #     num_fish_reset = sum(fish_to_be_reset)
        #     #add a new row of fish timer at 8
        #     current_pond = current_pond.append(pd.DataFrame({'fish_timer':8,'num_fish':num_fish_reset, 'day_num':day_num},index=range(1)),ignore_index=True)

        # print(current_pond)
        # break



main(18)