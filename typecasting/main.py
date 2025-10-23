# Typecasting = the process of converting a variable from one data type to another
#                     str(),int(),float(),bool()

name = "Bro Bhai"
age = 25
gpa = 5.6
is_student = True

# To check the data_type of variable

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

# Converting float to integer datatype
gpa = int(gpa)

print(gpa)

# Converting integer to float datatype
age = float(age)
print(age)

# Converting integer to string datatype

age = str(age)
# age += 1 ## TypeError: can only concatenate str (not "int") to str
# age += "1" this will give the output as ==> 251
print(age)

# Converting string to boolean
name = bool(name)

print(
    name
)  # this will give always true unless it's empty string which will give "false" output
# this can be used to check whether if someone has entered their name
