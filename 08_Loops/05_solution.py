input_str = str(input("Give me a string:\n "))

for char in input_str:
    print(char)
    if input_str.count(char) == 1 :
        print("CHAR IS: ", "'",char,"'")
        break
