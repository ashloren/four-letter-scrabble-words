# Input string
input_string = "UDON UDOS UGHS UGLY UKES ULAN ULNA ULUS ULVA UMBO UMMA UMPH UMPS UNAI UNAU UNBE UNCI UNCO UNDE UNDO UNDY UNIS UNIT UNTO UPAS UPBY UPDO UPON URBS URDS UREA URGE URIC URNS URPS URSA URUS USED USER USES UTAS UTES UVEA"

# Split the input string into a list of words
words = input_string.split()

# Convert the list to a formatted string
formatted_string = ', '.join(f'"{word}"' for word in words)

# Output the result
print(formatted_string)
