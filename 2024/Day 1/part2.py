# You have two lists of location IDs from day1.txt . Some numbers in each list appear in the other. 
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

right_count = Counter(right_list)

similarity_score = 0
for number in left_list:
    count_in_right_list = right_count[number]
    similarity_score += number * count_in_right_list

print(similarity_score)