"""
A number is a perfect square, or a square number, if it is the square of a positive integer.
For example, 25 is a square number because 5^2 = 5 x 5 = 25; it is also an odd square.

The first 5 square numbers are: 1, 4, 9, 16, 25, and the sum of the odd squares is 1 + 9 + 25 = 35 .

Among the first 259 thousand square numbers, what is the sum of all the odd squares?
"""
# 25 is a square
#print(pow(5, 2))

# The first five squares
"""
odd_sqr = 0
for num in range(1, 6):
    if num % 2 == 1:
        square = pow(num, 2)
        odd_sqr += square
print(odd_sqr)
"""
odd_sqr = 0
for num in range(1, 259001):
    if num % 2 == 1:
        odd_sqr += num ** 2
        
print(odd_sqr)

