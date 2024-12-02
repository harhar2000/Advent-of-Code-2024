# left_list and right_list
# sort both lists into ascending order
# pair the numbers and match them. smallest of each list together etc
# calculate difference
# add up total of all the differences

f = open("files/day1.txt")

left = []
right = []

with open("files/day1.txt") as f:
    for line in f:
        left, right = line.split()

        left.append(int(left))
        right.append(int(right))

left = []
right = []


left.sort()
right.sort()

pairs = zip(left, right)
    
total = 0
for a, b in pairs:
    total += abs(a - b)
print(total)

