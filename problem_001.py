"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these 
multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
# Natural numbers below 10 that are multiples of 3 or 5
"""
natural = list(range(1,10))
multiples = []
for num in natural:
    if num %3 ==0 or num%5 ==0:
        multiples.append(num)

# Sum of multiples is 23
print(sum(multiples))
"""

# Sum of all the multiples of 3 or 5 below 1000
natural = list(range(1,1000))
multiples = []
for num in natural:
    if num %3 ==0 or num%5 ==0:
        multiples.append(num)
print(sum(multiples))