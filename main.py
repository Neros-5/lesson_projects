# This is another calculator version using other means

from operators import add
from operators import subtract
from operators import multiply
from operators import divide

from others import cube
from others import square

# The above imports are functions of operators called from other files in the folder

operator = input("Give operator;")
if operator == 'square' or operator == 'Square' or operator == 'cube' or operator == 'Cube':
    num = eval(input("Enter number:"))
    if operator == 'square' or operator == 'Square':
        ans = square(num)
        print(ans)
    elif operator == 'cube' or operator == 'Cube':
        ans = cube(num)
        print(ans)
else:
    num1 = eval(input('Enter number 1:'))
    num2 = eval(input('Enter number 2:'))
    if operator == '+':
        ans = add(num1, num2)
        print(ans)
    elif operator == '-':
        ans = subtract(num1, num2)
        print(ans)
    elif operator == '*' or operator == "X" or operator == 'x':
        ans = multiply(num1, num2)
        print(ans)
    elif operator == '/':
        ans = divide(num1, num2)
        print(ans)
