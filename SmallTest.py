el_value = 0
tally = 1
d_list = [1, 2, 4, 1, 4, 6, 74, 2, 6, 8, 6, 3, 33, 57, 25, 25, 26, 84, 3]
while tally != len(d_list):
    print("Value to be eliminated is "+ str(d_list[el_value]))
    d_list.pop(el_value)
    print(d_list)
    print(len(d_list))
    tally += 1