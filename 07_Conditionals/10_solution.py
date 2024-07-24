Pet = str(input("Your Pet is A Dog or A Cat? \n"))
age = int(input("Tell me your pet's age? \n"))


if Pet == "Dog":
    print("Great,")
    if age <2 :
        print("Puppy Food")
    else: print("Dog Food")


if Pet == "Cat":
    print("Nice")
    if age >5 :
        print("Senior cat food")
    else: print("Kitten food")

print("THANK YOU!")