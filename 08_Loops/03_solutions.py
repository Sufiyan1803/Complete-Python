num = int(input("Give a number to prepare a multiplication table: "))

for i in range(1, 11):
    if i == 5:
        # To skip above iteration & continue further
        continue
    print(num, "x", i, "=", num*i)
