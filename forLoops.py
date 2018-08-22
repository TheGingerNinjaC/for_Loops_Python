'''
Author: Chané van der Berg
Date modified: 30/04/2018

Practical exercise aimed at solving problems using for loops.

Question 1:
-   Write a program that displays all values from 1 to n. The user nominates a
    value for n after which each integer is displayed up to the value included.

Question 2:
-   Write a Python program to do exponentiation of integer values. Write a
    function, powerInt() that accepts two integer values and returns the result
    of the first value raised to the power of the second. The integer result is
    returned to the calling statement. When writing powerInt(), you are not
    allowed to use any functions of the math.py module or use the power
    operator (**). Use for loops to determine the result. Use the powerInt()
    function to produce output.

Question 3:
-   Write a function, mathTable(), which receives an integer and displays the
    multiplication table for the number up to 12.
-   Use the function in a program to display its operation.

'''

# Question 1

n = int(input("Enter the number of values to display: "))

for count in range(n):
    print(count + 1)

print()

# Question 2

base = int(input("Enter base value: "))
exp = int(input("Enter exponent value: "))

def powerInt(base, exp):
    num = 1
    for powerInt in range(exp):
        if exp > 0:
            num = num * base
        if exp < 0:
            num = 1 / (num * base)
    return num

print(str(base),"raised to the power of",str(exp),"=",str(powerInt(base, exp)))

print()

# Question 3

def mathTable(x, y):
    for x in range (1, x + 1):
        for y in range (1, y + 1):
            z = x * y
            print(z, end="\t")
        print()

row = int(input("Enter value for multiplication table: "))
col = 10

mathTable(row,col)
