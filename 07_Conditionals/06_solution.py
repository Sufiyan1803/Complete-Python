print("Transportation Mode Selection \n")

Distance = int(input("Distance in km:  "))

if Distance <3 :
    print("Walk")
elif Distance <=15 :
    print("Bike")
elif Distance >15 :
    print("Car")