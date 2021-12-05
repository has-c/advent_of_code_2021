import os
import numpy as np
from numpy.lib import index_tricks

def read_in_file(filepath):
    f = open(filepath, "r")
    content = f.readlines()
    return content

def run_bingo(all_boards,control_number_sequence):
    solved = False
    original_boards = all_boards.copy()
    for num in control_number_sequence:
        # print(num)
        if not(solved):
            #cross off relevant boards
            for idx in range(len(all_boards)):
                board = all_boards[idx]
                for col in range(board.shape[1]):
                    board[board[:,col] == num, col] = -1

                #after each number is ticked off on a board
                #check boards for completion
                #row and col check
                for col_idx in range(board.shape[1]):
                    col_sum = sum(board[:,col_idx])
                    if col_sum == -5:
                        solved = True
                        board_idx = idx
                        winning_num_called = num
                for row_idx in range(board.shape[0]):
                    row_sum = sum(board[row_idx,:])
                    if row_sum == -5:
                        solved = True
                        board_idx = idx
                        winning_num_called = num

        else:   
            break

    return all_boards,board_idx,winning_num_called

def main():
    filepath = r"day_4_puzzle_input.txt"
    data = read_in_file(filepath)

    #create boards and control number sequence
    control_number_sequence = data[0].strip("\n").split(",")
    control_number_sequence = [int(num) for num in control_number_sequence]

    raw_boards = data[1:]
    board = []
    all_boards = []
    num_board_rows = 5
    for line in raw_boards:
        board_line = line.strip("\n").split(" ")
        if len(board_line) > 1:
            #clean line
            board_line = [int(char) for char in board_line if char != '']
            #add line to board
            board.append(board_line)
            if len(board) == num_board_rows:
                #full board
                all_boards.append(np.array(board))
                board = []

    #run bingo and check for completed boards
    last_winning_boards = all_boards.copy()
    while len(last_winning_boards) > 0:
        modified_boards,winning_board_idx,winning_num_called = run_bingo(last_winning_boards,control_number_sequence)
        #remove winning board
        if len(last_winning_boards) == 1:
            #grab last board
            loosing_board = modified_boards[0].copy()
        last_winning_boards.pop(winning_board_idx)
        
    print(loosing_board)
    #calculate winning board sum
    score_unmarked_numbers = sum([num for num in loosing_board.flatten() if num != -1])
    total_score = score_unmarked_numbers * winning_num_called
    print(winning_num_called)
    print(score_unmarked_numbers)
    print(total_score)
        

    

main()