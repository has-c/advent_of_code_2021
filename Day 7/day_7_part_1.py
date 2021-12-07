import os
import numpy as np


def read_in_file(filepath):
    f = open(filepath, "r")
    content = f.readlines()
    return content

def main():
    filepath = r"day_7_puzzle_input.txt"
    data = read_in_file(filepath)
    data = [int(pos) for pos in data[0].split(",")]

    max_horizontal_position = max(data)
    min_horizontal_position = min(data)
    fuel_required = []
    for pos in range(min_horizontal_position, max_horizontal_position+1):
        #for each pos find cost of moving all crabs to that spot
        fuel_required_for_pos = [abs(og_pos - pos) for og_pos in data]
        fuel_required.append(sum(fuel_required_for_pos))
    
    optimal_pos = min_horizontal_position + fuel_required.index(min(fuel_required))
    print(min(fuel_required))
    print(min_horizontal_position + fuel_required.index(min(fuel_required)))

main()