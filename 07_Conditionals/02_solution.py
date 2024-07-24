# age = int(input("Tell me your age: "))
# day = str(input("Tell me day for ticket price:"))

# price = 12 if age >= 18 else 8

# if day == "Wednesday":
#     # price = price - 2
#     price -= 2
# else: print(price)

# print("Your Ticket price is $", price )









name  = 'Movie Ticket Pricing'
print(name)

age = int(input("\nTell me your age: "))

day = str(input("Tell me a day you are looking for movie ticket: "))
price = 12 if age > 17 else 8

if day == 'Wednesday':
    price -= 2
else:
    pass

print("Your ticket price is $", price)









