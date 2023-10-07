# Original list of lists containing letters
list_ = [['A','B','C'], ['D','E','F'],['G','H','I']]

# Initialize an empty list 'list_s' to store the modified lists
list_s = []

# Loop through each sublist in 'list_'
for letter in list_:
    # Check if 'G' is not in the sublist
    if 'G' not in letter:
        # If 'G' is not in the sublist, append the sublist to 'list_s'
        list_s.append(letter)
    else:
        # If 'G' is in the sublist, append a message indicating it was skipped
        list_s.append('Letter was skipped')

# Print the modified list
print(list_s)
print('X' * 20)

# Using list comprehension to achieve the same result as above
list_sc = [letter for letter in list_ if 'G' not in letter]

# Print the modified list
print(list_sc)

print('x' * 20)

# Using a conditional expression within list comprehension to achieve the same result as above
list_scx = [letter if 'G' not in letter else 'Letter was skipped' for letter in list_]

# Print the modified list
print(list_scx)
