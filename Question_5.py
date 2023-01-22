import math
radius=30
#finding the area of circle with radius value 30
_area_of_circle_=math.pi*pow(radius,2)
print("area of circle is:""{:.2f}".format(_area_of_circle_))
#finding the circumference of circle with radius value 30
_circum_of_circle_=2*math.pi*radius
print("circumference of circle is:""{:.2f}".format(_circum_of_circle_))
#Taking radius as input and calculating the area
radius=int(input("Enter the radius:"))
area_circle=math.pi*pow(radius,2)
print("area of circle is:""{:.2f}".format(area_circle))