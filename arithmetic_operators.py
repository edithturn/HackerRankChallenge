import random

# Task
# The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.
# Example
# Print the following:
# 8
# -2
# 15

if __name__ == '__main__':
    for i in range(0 , 5):
        a = random.randint(1, 6)
        b = random.randint(1, 6)
    print(a + b)
    print(a - b)
    print (a * b)