import os

def read_in_file(filepath):
    f = open(filepath, "r")
    content = f.readlines()
    return content

def main():
    filepath = "day_1_puzzle_input.txt"
    content = read_in_file(filepath)

    #create window length 3 sums
    window_sums = []
    window = []
    for depth in content:
        if len(window) < 3:
            window.append(int(depth.split("\n")[0]))
        
        if len(window) == 3:
            window_sums.append(sum(window))
            #reduce window
            window = window[1:]
    
    prev_sum = window_sums[0]
    num_window_increases = 0
    for windowed_sum in window_sums:
        if windowed_sum > prev_sum:
            num_window_increases += 1
        prev_sum = windowed_sum

    print(num_window_increases)

main()