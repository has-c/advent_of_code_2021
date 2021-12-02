import os

def read_in_file(filepath):
    f = open(filepath, "r")
    content = f.readlines()
    return content

def main():
    filepath = "day_2_part_1_input.txt"
    data = read_in_file(filepath)
    
    horizontal = 0
    depth = 0
    aim = 0

    for move in data:
        move = move.strip("\n")
        move_components = move.split(" ")
        move_dimension = move_components[0]
        move_value = int(move_components[1])

        if "forward" in move_dimension:
            horizontal += move_value
            depth += (aim*move_value)

        elif "up" in move_dimension:
            aim -= move_value

        elif "down" in move_dimension:
            aim += move_value

    
    print("horizontal ", horizontal)
    print("depth ", depth)
    print("product ", horizontal * depth)

main()