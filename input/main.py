"""

input() ==> A Function that prompts the user to enter data
               # Returns the entered data as a string
               #
"""

from posix import PRIO_PROCESS


name = input("What is your name?: ")
age = int(input("How old are you?: "))
# while taking the input convert into integer

# age = int(age)  # first convert into integer to add
age = age + 1

print(f"Hello {name}")
print("HAPPY BIRTHDAY!")
print(f"You are {age} years old")

##################################### Calculate the area of rectangle #########################################
# Exercise 1
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width

print(f"The area of rectangle is {area}cm²")

#################################### Exercise 2 (Shopping Cart Program)########################################

item = input("What item would you like to buy? :")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?"))
total = price * quantity
print(total)

print(f"You have bought {quantity} x {item}/s")
print(f"Your Total is : {total}")
