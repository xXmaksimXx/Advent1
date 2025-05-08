report = []
row = []

with open(r"C:\Users\mpecherskiy\Documents\CS\Python\Input_files\Advent_2.txt") as f:
    for line in f:
        # Split line into string tokens, convert each to int, and append as a list (row)
        row = [int(x) for x in line.strip().split()]
        report.append(row)