row = []
report = []

with open(r"C:\Users\mpecherskiy\Documents\CS\Python\Input_files\Advent_2.txt") as f:
    for line in f:
        # Split line into string tokens, convert each to int, and append as a list (row)
        row = [int(x) for x in line.strip().split()]
        report.append(row)


i = 0                      #initialize the row counter
k = 0
difference = 0             #initialize difference value 
safety_matrix = []
safety_report = {}

for row in report:                                           #for each row
    print("Checking " + str(row))
    j = 0                                                    #initialize the column counter (this brings us to the individual value in the row)
    for value in report[i]:                                  #and for each value in the row                                      
        print("We are going to check the value " + str(report[i][j]))                         
                                                       
        if j == len(report[i]) -1:                          #if the column counter is the same length as the row, break out of the of this code because 
            safety_matrix.append("Safe")
            print(str(report[i][j]) + " is the last value in the current row:" + str(report[i]) )
            print("This line is safe!")
            break                                        
        

        difference = report[i][j] - report[i][j + 1]        #"difference" is the difference between the current value in the array row and the next value 
        #print("The difference between " + str(report[i][j]) + " and " + str(report[i][j + 1]) + " is " + str(difference))

        if abs(difference) > 3:                             #if the magnitude of difference is too high, break out
            safety_matrix.append("Unsafe")
            break

        
        if j == 0:                                          #if we are at the first value in the row
            if difference > 0:                              #let's determine whether we should continue to increase or decrease as we progress through the row based on the first difference
                k = 1
            elif difference < 0 :
                k = -1
            else: 
                
                print("The difference was 0! Yikes!")
                safety_matrix.append("Unsafe")
                break

        else:                                              #make sure we are constantly increasing or constantly decreasing
            if difference > 0 and k == -1:
                print("Difference was expected be negative, but was positive.")
                
                safety_matrix.append("Unsafe")
                break
            elif difference < 0 and k == 1:
                print("Difference was expected be posiive, but was negative.")
                safety_matrix.append("Unsafe")
                break
            elif difference == 0:
                print("The difference was 0! Yikes!")
                safety_matrix.append("Unsafe")
                break
        j += 1


    i += 1
    j = 0



for entry in safety_matrix:
    if entry not in safety_report.keys():
        safety_report[entry] = 1
    else:
        safety_report[entry] += 1

print(safety_report)