

# ex_list = [3, 5, 0, 6, 3, 7, 8, 7, 9, 0]

# counts = Counter(ex_list)

# print(counts[0]) # = 2


# You have two lists of location IDs from part1.py . Some numbers in each list appear in the other. 
# Calculate how similar the two lists are

# For each number in the left list, check how many times it appears in the right.
# Multiply the number by the count of its appearance in the right list
# add up the results to get the total similarity score

from collections import Counter

left_list = []
right_list = []


with open("2024/files/day1.txt") as f:
    for line in f:
        left, right = line.split()

        left_list.append(int(left))
        right_list.append(int(right))



counts = Counter(right_list)
    
print(counts)