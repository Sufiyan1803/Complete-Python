
chai_types = {"Masala":"Spicy", "Ginger":"Zesty", "Green":"Lemon"}
print(chai_types)


chai_types["Ginger"]

 # to access key
chai_types.get("Green")


 # change value
chai_types["Green"] = "Fresh"


 # loopss

for chai in chai_types:
    print(chai)
#  this only print key values


#   print key along with values
for chai in chai_types:
    print(chai, chai_types)


for key, value in chai_types.items():
    print(key, value)

chai_types["Earl grey"]= "Citrus"
print(chai_types)


# to pop specific value
chai_types.pop("Ginger")

# to pop last item
chai_types.popitem()




# to remove value from memory
del chai_types["Green"]



squared_nums = {x:x**2 for x in range(10)}
print(squared_nums)

# squared_nums.clear()



# combine and make new dict
keys= {"masala", "ginger", "lemon"}
default_value="Delicious"

new_dict= dict.fromkeys(keys, default_value)
print(new_dict)