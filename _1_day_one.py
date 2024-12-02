# left_list and right_list
# sort both lists into ascending order
# pair the numbers and match them. smallest of each list together etc
# calculate difference
# add up total of all the differences

left_list = []
right_list = []


with open("files/day1.txt") as f:
    for line in f:
        left, right = line.split()

        left_list.append(int(left))
        right_list.append(int(right))

# print("Left list:", left_list)
# print("Right list:", right_list)


left_list.sort()
right_list.sort()

pairs = zip(left_list, right_list)
    
total = 0
for a, b in pairs:
    total += abs(a - b)
print(total)

