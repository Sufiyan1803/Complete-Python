# ---------------------------------------------------------
print('-------------------Sets---------------')
# Sets are used to store multiple items in single variable
# A set is a collection which is unordered, unchangeable and unindexed
# Sets are written in curly braces {}

setone = {'apples', 'mangoes', 'banana'}
print(setone)

# Unordered means that the item in a set do not have a defined order, it can appear in different order every time you use them, and cannot be refered to by index or key

# Unchangeable means we cannot change the items after the set has been created but we can remove and add new items

# Sets do not allows duplicate values, dv will be ignored

settwo = {1, 2, 3, 4, 5, 3, 2, 7, 1, 2, True}
print(settwo) # {1, 2, 3, 4, 5, 7}

# get the length of set
print(len(settwo)) # 6

# type of set
print(type(settwo)) # <class 'set'> Defined as objects

# Set constructor
setthree = set((10, 20, 30, 40, 50, 60)) # double round brackets
print(setthree)



# SET
setone = {1, 2, 3, 4}


# intersection
print(setone & {1,2,5})


# union
print(setone | {1,2,5})


# Empty set is Dictionary
print(setone - {1,2,3,4})


# Used to define type
e=type({})
print(e)


# BOOLEAN
q = type(True)
print(q)
