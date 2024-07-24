num = int(input("Give me Number: "))
fact = 1

while num > 0:
    # fact = fact * num
    # num = num - 1

    fact *= num
    num -= 1

print("Factorial value of given number is: ", fact)