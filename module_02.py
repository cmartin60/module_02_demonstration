"""
Description: Module 02 Demonstration
Author: Christian Jorge R. Martin
Date: 16 January 2024
Usage: Demonstrate content from Module 02
"""
# - Single-line comment

# Constants
PI = 3.14159
FEDERAL_TAX_RATE = 0.05

#Purely convention; these can be change


# -Function-
# A unit of code that can be re-used repeatedly
# () parentheses contains "arguments"
# the function runs using the arguments that have been provided
print("Test Value")

# order of operations
# evaluates (finds the outcome) of the operation before using it as an argument
print(3 + 3)

# -Abs Function- 
#"Absolute value" of number argument

# argument: -50
# "Invocation": when a function is "called" or "used"
# "return value": the value that the function invocation is evaluated 
# to/replaced by
print (
    abs(-50) # output = 50
    )

# abs make the output to 50 hence it will become pring (50)
print("I am", 25, "years old")

"""
DATA TYPES
"""
# -Variables-
# something used for storing a value

# DECLARE variable "number_a" and ASSIGN value of 12
number_a = 12

# RE-ASSIGN number a with value 13
number_a = 13
number_b = 25

# declare number_sum and assign it the evaluation of number_a + number_b values
number_sum = number_a + number_b
print (number_sum)

# -Variable Type-
# -Numeric Type-
    # -integer- -- whole number
new_int = 32

    # -floating points- -- decimal number
new_float = 32.7

# -Text Type-
    # -strings- -- collections of characters
new_str = "This is a string"
new_str = False

# -Boolean Type-
new_bool = False
print(type(new_bool))

# Programming Languages are typically either DYNAMICALLY or STRICTLY typed

age = 25
current_salary = 67293.21

# "implicity" convert age to a float for this ogeration
age_and_salary = age + current_salary
print(age_and_salary)

months = "11"
years = 25
# explicit conversion:
print(int(months) + years)
print(months + str(years))
print("a" + "b")

# String methods
original_string = "hello world"

original_string = original_string.capitalize() # assign original_string variable to the return value of original_string.captialize()
print(original_string)

"""
Find the arguments that must be passsed and return values of these string methods
center() -- center (length,character)
startswitch() -- startswitch (character)
endswitch()
upper(), lower()
len() -- len (length)
"""

teststring = "testing string"
teststring = teststring.center(30, "-")

startswitchvalue = teststring.startswith("-")
teststringlength = len(teststring)

print(teststringlength)


"""
+
-
*
/
// -- removes the remainder
% -- print out the remainder
** -- gives out the power of
=
"""

print(12 * 5)
firstnumber = 12 
firstnumber += 10   # performs the function to the given value
print(firstnumber)

"""
Collections
"""
# LIST EXAMPLE -  uses: []
daily_step_count = [[0,1], [3,4], [7,8]] # 0, 1, 2
daily_step_count.append("test")
print(daily_step_count[len(daily_step_count) - 1])

daily_step_count = ["zero", "one" , 2] # 0, 1, 2
daily_step_count.append("test") # add value at the end of the index
# if pop argument is empty () it removes the last item in the index
daily_step_count.pop(0) # remove item from the index
daily_step_count.insert(1, "zero and a half") # inserts object before index
print(daily_step_count)

daily_step_count = ['R', 'R', 'C', '', 'P', 'o', 'l', 'y', 't', 'e', 'c', 'h', 'n', 'i', 'c'] # 0, 1, 2, 3
print(daily_step_count[3:15:2])

#TUPLE EXAMPLE - uses: ()
provinces = ("AB", "MB", "SK", "BC") # 0, 1, 2, 3
manitoba = provinces[1] # tuple
print (manitoba)


# variable name - list_var
# value -collection/list ["zero", "one", "two", "three", "four", "five", "six"]
# elements - "zero", "one", "two", "three", "four", "five", "six"
# length - 7
# elements = index
list_var = ["zero", "one", "two", "three", "four", "five", "six"]

#DICTIONARY EXAMPLE - uses: {}
new_dictionary = {
    'days_in_week':7,
    'days_in_year':365,
    'minutes_in_hour': 60
}

print(new_dictionary["days_in_week"])
print(new_dictionary.keys())
# .keys() shows the keys in the dictionary
# .value() shows the value in the dictionary
# .items() shows the keys and the value in the dictionary

#SET EXAMPLE - index reference of not repeating values - uses: {}
#all of the values in a set should be unique
primes = {2, 3, 3, 5, 7, 8, 6,}
print (primes)
primes.remove(6) # error if element doesnt exist
primes.discard(10) # no error if doesnt exist


