d_list = [1, 2, 4, 1, 4, 6, 74, 2, 6, 8, 6, 3, 33, 57, 25, 25, 26, 84, 3, 3, 3]
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

