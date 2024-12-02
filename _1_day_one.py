# left_list and right_list
# sort both lists into ascending order
# pair the numbers and match them. smallest of each list together etc
# calculate difference
# add up total of all the differences


def difference_calc(left, right):
    left.sort()
    right.sort()

    pairs = zip(left, right)
    

    for a, b in pairs:
       difference = abs(a -b)



 
