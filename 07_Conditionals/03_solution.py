score = int(input("Tell me your score: "))

if score >=101 :
    print("Verify your score!")
    exit()

    
if 100>=score>=90 :
    print("Your grade is: A")

elif score>=80 :
    print("Your grade is: B")

elif score>=70 :
    print("Your grade is: C")

elif score>=60 :
    print("Your grade is: D")

else : print("Your grade is: F","\nYOU ARE FAIL!")