# specific char
chai= "Masala chai"
first_char = chai[0]
print(first_char)

# slice
chai='Masala chai'
slice_chai = chai[0:6]
print(slice_chai)
  
 
# num_list = "0123456789" 
# num_list[:]
# '0123456789'
# num_list[3:] 
# '3456789'
# num_list[3:8]
# '34567'
# num_list[0:7:2]
# '0246'
# num_list[0:7:3] 
# '036'
  
 



# lower & upper
chai='Masala chai'
print(chai.lower())

print(chai.upper()) 
  

#  strip

chai = "   Masala chai   "
print(chai.strip())






# replace
chai='Lemon chai'
print(chai.replace("Lemon" , "Ginger"))






# split (string to list conversion)
chai = 'Lemon, Ginger, Masala, Mint'
chai
'Lemon, Ginger, Masala, Mint'
print(chai.split(", "))
# ['Lemon', 'Ginger', 'Masala', 'Mint']






# find
chai
'Masala chai'
print(chai.find("chai"))
7
print(chai.find("Chai")) 
-1
chai
'Masala chai'
chai = "Masala chai chai chai"
chai
'Masala chai chai chai'
print(chai.count("chai"))
3










# order formatting
chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai"
order
'I ordered {} cups of {} chai'

print(order.format(quantity,chai_type))












# List to string conversion
chai_variety = ["Lemon", "Masala","Ginger"]

print("".join(chai_variety))

print(" ".join(chai_variety))

print("-".join(chai_variety))  

print(", ".join(chai_variety))










# length 
chai="Masala chai"
chai
'Masala chai'
print(len(chai))
11
chai
'Masala chai'
for letter in chai:
     print(letter)

# M
# a
# s
# a
# l
# a

# c
# h
# a
# i







# Used for pathing 
chai="He said, \"Masala chai is awesome\"" 
print(chai)

chai="Masala\nchai"
print(chai)

chai=r"Masala\nchai"
print(chai)








# True ,False
chai="Masala chai"

print("Masala" in chai)
True
print("Masalaa" in chai)
False
