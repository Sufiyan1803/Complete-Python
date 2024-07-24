PassWord = input("PassWord: ")
PassWord_length = len(PassWord)

if len(PassWord) < 6 :
    print("Strength is Weak")
elif len(PassWord) <=10 :
    print("Strength is Medium")
elif len(PassWord) >10 :
    print("Strength is Strong")