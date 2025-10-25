import math

# a = pi r 2
radius = float(input("Enter a radius :"))

# Area = math.pi * radius**radius
Area = math.pi * pow(radius,2)


print(f"The Area of this circle is {round(Area,2)}cm²")
