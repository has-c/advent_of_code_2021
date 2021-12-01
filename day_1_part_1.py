import os

def read_in_file(filepath):
    f = open(filepath, "r")
    content = f.readlines()
    return content

def main():
    filepath = "day_1_puzzle_input.txt"
    content = read_in_file(filepath)

    #run algo to find number of depth increases
    num_depth_increases = 0
    prev_depth = int(content[0].split("\n")[0])
    for depth in content:
        current_depth = int(depth.split("\n")[0])
        if current_depth > prev_depth:
            num_depth_increases += 1
        prev_depth = current_depth
    

    print(num_depth_increases)

main()