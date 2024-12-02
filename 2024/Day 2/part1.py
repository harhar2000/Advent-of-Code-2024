# Determine whether each report in a list is "safe" based on specific rules

# Each line of numbers is a report

# To be safe the report must meet two conditions:

#   1. All levels must be consequetively increasing or consequetively decreasing.
#   2. The difference between any two adjacent numbers must be between 1 and 3.
#       e.g. 7 to 6 is difference of 1, which is okay. 7 to 4 is difference of 3, which is okay. 
#           7 to 3 (difference of 4) is not okay.

# Check each report against these rules and count how many reports are considered safe. 






# with open("2024/files/day1.txt") as f:
#     for line in f:
