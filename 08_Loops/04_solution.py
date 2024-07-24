

print("REVERSE A STRING\n")

input_string = str(input("Give an input String:  "))
reversed_string = ""

for char in input_string:
    reversed_string = char + reversed_string

print("Your Reversed String is: ", reversed_string)
