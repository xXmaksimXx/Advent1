import numpy as np

def import_data_builtin(filepath):
    """Imports two-coloumn data from a text file into two separate lists sing built-in Python
    
    Args:
        Filepath (str): The path to the text file
        
        Returns:
        tuple: A tuple containing two lists, list1 and list2
            Returns (None, None) if there's an error opening the files"""
          
    list1 = []
    list2 = []

    try:
        with open(filepath) as f:
            for line in f:
                columns = line.strip().split('   ') #adjust split() based on your delimeter
                list1.append(int(columns[0]))
                list2.append(int(columns[1]))
    except:
            print(f"Error: File not found at {filepath}")
            return None, None
    return list1, list2

list1 = []
list2 = []                     #intialize lists
i = 0                          #initialize a counter                 
distance_difference = []       #initialize an array to hold distance deltas 

uniques = []                   #initialize an array to hold unique values
ss = 0                         #initialize simularity score

path = r"C:\Users\mpecherskiy\Documents\CS\Python\Input_files\Advent_1.1.txt"       #establish the path 
list1, list2 = import_data_builtin(path)                                            #put values from text file in list1 and list2


list1c = list1                #make our own copies of the lists
list2c = list2

list1c.sort()                 #sort the lists from least to greatest
list2c.sort()

#print(list1c)                 #check the new lists
#print(list2c)                

for value in list1c:                                        #for each value in the list1c array
    difference = abs(list2c[i] - value)                     #calculate the difference between the current 1ist1c value and the corresponding list2c value
    distance_difference.append(difference)                  #append the value to the distance array
    i += 1                                                  #and increase the counter by 1
    #print(distance_difference)                                  

final_distance = sum(distance_difference)                   #sum all all values in the distance array to get the total distance
print(final_distance)


for number in list1c:
   if number not in uniques:
      uniques.append(number)


for number in uniques:
    i = 0
    for value in list2c:
        if number == value:
            i += 1
    ss += i * number
print(ss)

'''
tally2 = 0                                                                                      #check this value for duplicate

while tally2 < len(d_list):                                                                    # as long as we have not checked every number in the list 

    tally = tally2 + 1                                                                          #we always want to start searching for duplicates starting with the value following our chosen value
    print("Currently evaluating whether " + str(d_list[tally2]) + " has any duplicates") 

    while tally < len(d_list):                                                                   # as long as we have not checked every number in the list 

        print("Currently evaluating whether " + str(d_list[tally]) + " is a duplicate of " + str(d_list[tally2])) 

        if d_list[tally2] != d_list[tally]:                                                    #if the current tally value is not equal to the value we are checking for duplicates 
         print(str(d_list[tally]) + " is not a duplicate of " + str(d_list[tally2]))
         tally += 1                                                                            #continue to the see whether the next value is a duplicate
        else:                                                                                  #otherwise
         print("Removing " + str(d_list[tally]) + " from " + str(d_list))
         d_list.pop(tally)                                                                      #remove the value entirely
         print("The new list is: " + str(d_list))

        
    tally2 += 1                                                                               #lets check for duplicates for the next value in the list 

print(d_list)

#https://www.youtube.com/watch?v=_uQrJ0TkZlc
#in youtube video "Python Full Course for Beginners", the solution is as follows:
solution_list = [5, 2, 1, 5, 7, 25, 34, 1, 1, 5, 11, 6, 10, 11, 7, 8]
uniques = []
for number in solution_list:
   if number not in uniques:
      uniques.append(number)
print(uniques)

'''


