# Asking for the first and second numbers, and immediately making them integers
first_num = int(input("Please input the first number! "))
second_num = int(input("Please input the second number! "))

# Saving the sum of the two numbers
sum_of_numbers = first_num+second_num

# Saving the difference between the two numbers
diff_of_numbers = first_num-second_num

# Saving the product of the two numbers
product_of_numbers = first_num*second_num

# Saving the quotient of the two numbers. If it divides by zero, it will instead change the variable to a string
# saying it is unable to divide by zero. Another way of handling this would be to not allow zero to be entered
# at the beginning and raise an exception if either of the numbers are zero.
try:
    quotient_of_numbers = first_num/second_num
except ZeroDivisionError:
    quotient_of_numbers = "Unable to divide by zero."\

# Outputting all the variables using f strings, as they are more efficient than .format or regular concatenation
print(f'''The sum of the numbers is: {sum_of_numbers}
The difference of the numbers is: {diff_of_numbers}
The product of the numbers is: {product_of_numbers}
The quotient of the numbers is: {quotient_of_numbers}''')

