list_varieties = ["Black", "Green", "White","Oolong"]
print(list_varieties)


# slicing can also be done
slice_list = list_varieties[1:4]
print(slice_list)



# loops
for list in list_varieties:
    print(list)



# for list in list_varieties:
    # print(list, end="-")
    
    



# conditionals

if "Oolong" in list_varieties:
    print("I have Oolong")



if "Masala" in list_varieties:
    print("Masala")
else: print("I dont have this in the list")





# Methods:
# To add something in list at the end 
list_varieties.append("Masala")
print(list_varieties)


# To remove end value from list
list_varieties.pop()
print(list_varieties)



# To remove value from list
list_varieties.remove("White")
print(list_varieties)


# To insert value in list
list_varieties.insert(2, "Masala")
print(list_varieties)




# To make different reference in memory
list_varieties_copy = list_varieties.copy()
list_varieties.append("Lemon")
print(list_varieties_copy)




# for square and cube values by defining range of numbers
squared_nums = [x**2 for x in range(10)]
print(squared_nums)


cube_nums = [y**3 for y in range(5)]
print(cube_nums)










