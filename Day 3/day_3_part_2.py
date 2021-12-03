import os
import numpy as np
from scipy import stats

def read_in_file(filepath):
    f = open(filepath, "r")
    content = f.readlines()
    return content

def mcb_filter(report_array,num_ones,num_zeros,bit_num):
    if num_ones > num_zeros:
        #mcb is 1 
        mcb = "1"
    elif num_ones < num_zeros:
        mcb = "0"
    else:
        mcb = "1"
    
    report_array = report_array[report_array[:,bit_num] == mcb]
    return report_array

def lcb_filter(report_array,num_ones,num_zeros,bit_num):
    if num_ones > num_zeros:
        #lcb is 1 
        lcb = "0"
    elif num_ones < num_zeros:
        lcb = "1"
    else:
        lcb = "0"
    
    report_array = report_array[report_array[:,bit_num] == lcb]
    return report_array

def filter(report_array, is_mcb):
    num_bits = report_array.shape[1]
    num_examples = report_array.shape[0]

    for bit_num in range(num_bits):
        num_zeros = np.count_nonzero(report_array[:,bit_num] == "0")
        num_ones = num_examples - num_zeros

        if is_mcb:
            report_array = mcb_filter(report_array,num_ones,num_zeros,bit_num)
        else:
            report_array = lcb_filter(report_array,num_ones,num_zeros,bit_num)
        
        if report_array.shape[0] == 1:
            return report_array

        num_examples = report_array.shape[0]

    return report_array


def main():
    filepath = r"day_3_puzzle_1_input.txt"
    data = read_in_file(filepath)

    #assemble matrix
    report = []
    for line in data:
        line = line.strip("\n")
        line_array = list(line)
        report.append(line_array) 
    report_array = np.array(report)

    #oxygen and co2 ratings
    mcb_report_array = report_array.copy()
    lcb_report_array = report_array.copy()

    oxygen_sequence = filter(mcb_report_array, True)
    co2_seqeuence = filter(lcb_report_array, False)
    print(oxygen_sequence)
    print(co2_seqeuence)

    oxygen_binary = "".join(list(oxygen_sequence[0]))
    co2_binary = "".join(list(co2_seqeuence[0]))

    oxygen_rate = int(oxygen_binary,2)
    co2_rate = int(co2_binary,2)

    #life support
    life_support = oxygen_rate * co2_rate

    print(oxygen_rate)
    print(co2_rate)
    print(life_support)

main()