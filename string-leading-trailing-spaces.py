# Given string
s:str = "   Python is fun!   "

# Remove leading and trailing spaces
trimmed_s = s.strip()

# Left justify with '*'
left_justified = trimmed_s.ljust(20, '*')

# Right justify with '*'
right_justified = trimmed_s.rjust(20, '*')

# Print the results
print(f"Original string: '{s}'")
print(f"Trimmed string: '{trimmed_s}'")
print(f"Left justified: '{left_justified}'")
print(f"Right justified: '{right_justified}'")
