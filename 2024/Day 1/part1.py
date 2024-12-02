# The Chief Historian's absence could jeopardise the Christmas sleigh launch! 
# Senior elves found two incomplete lists of locations, each identified by a unique location ID. 
# These lists represent two different searches, but they need to be reconciled to ensure no location is missed.

# Compare the two lists and measure how far apart they are.

# 1. Sort Both Lists: into ascending order.
# 2. Pair Numbers: Match smallest number from left list with smallest from right list and so on
# 3. Calculate Differences: For each pair, calculate the absolute difference between the two numbers.
# 4. Add Differences: Sum up all the differences to find the total distance 

### Example:
# Given:
# - Left list: [3, 4, 2, 1, 3, 3]
# - Right list: [4, 3, 5, 3, 9, 3]

# Steps:
# 1. Sorted left: [1, 2, 3, 3, 3, 4]
# 2. Sorted right: [3, 3, 3, 4, 5, 9]
# 3. Pairs: (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (4, 9)
# 4. Differences: 2, 1, 0, 1, 2, 5
# 5. Total Distance: = 11



left_list = []
right_list = []


with open("2024/files/day1.txt") as f:
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

