import os
import numpy as np
import pandas as pd

def read_in_file(filepath):
    f = open(filepath, "r")
    content = f.readlines()
    return content

def main():
    filepath = r"day_5_puzzle_input.txt"
    data = read_in_file(filepath)

    #each line in txt is a vent line
    #create board based on max y and x values
    
    lines_to_plot = [point.strip("\n") for point in data]

    #find max x and max y
    from_points = np.array([point.split(" -> ")[0] for point in lines_to_plot])
    from_points = [point.split(",") for point in from_points]
    from_points = np.array(from_points).astype(int)

    to_points = np.array([point.split(" -> ")[1] for point in lines_to_plot])
    to_points = [point.split(",") for point in to_points]
    to_points = np.array(to_points).astype(int)

    max_x = max(np.append(to_points[:,0], from_points[:,0]))
    max_y = max(np.append(to_points[:,1], from_points[:,1]))

    #create preallocated grid
    grid = np.zeros((max_y+1,max_x+1))

    for idx in range(from_points.shape[0]):
        from_point = from_points[idx,:]
        to_point = to_points[idx,:]

        if from_point[0] == to_point[0]: #line is vertical
            if from_point[1] < to_point[1]:
                grid[from_point[1]:to_point[1]+1,from_point[0]] += 1
            else:
                grid[to_point[1]:from_point[1]+1,from_point[0]] += 1
            
        elif from_point[1] == to_point[1]: #line is horizontal
            if from_point[0] < to_point[0]:
                grid[from_point[1], from_point[0]:to_point[0]+1] += 1
            else:
                grid[from_point[1], to_point[0]:from_point[0]+1] += 1
        else:
            #diagonal line 
            #get equation of line and create points to fill in - RIP could have done this for the vert/horizontal too
            m = (from_point[1]-to_point[1])/(from_point[0]-to_point[0])
            c = from_point[1] - (m*from_point[0])
            #create all points in between and fill in
            points = []
            for x in range(min(from_point[0],to_point[0]),max(from_point[0],to_point[0])+1):
                point_x = int(x)
                point_y = int(m*x+c)
                grid[point_y,point_x] += 1

    # examine grid 
    num_overlaps = np.sum(grid > 1)
    print(num_overlaps)
    
main()