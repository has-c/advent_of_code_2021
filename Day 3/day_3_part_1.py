import os
import numpy as np
from scipy import stats

def read_in_file(filepath):
    f = open(filepath, "r")
    content = f.readlines()
    return content

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

    #gamma and epsilon arrays
    num_bits = report_array.shape[1]
    gamma_array = [stats.mode(report_array[:,bit_num])[0][0] for bit_num in range(num_bits)]
    gamma_binary = "".join(gamma_array)
    epsilon_array = ['0' if bit == '1' else '1' for bit in gamma_array]
    epsilon_binary = "".join(epsilon_array)

    #convert binary to decimal
    gamma_rate = int(gamma_binary,2)
    epsion_rate = int(epsilon_binary,2)

    #power consumption
    power_consumption = gamma_rate * epsion_rate

    print(gamma_rate)
    print(epsion_rate)
    print(power_consumption)
main()