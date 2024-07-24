import math

def circle(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference


a, c= circle(int(input("Give me a value for circle radius: ")))

print("Area of Circle: ", round(a,2) , "&", "Circumference of Circle: ", round(c,2) )



