'''
This problem was asked by Facebook.

Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
'''
from itertools import permutations
lst=map(int,input().split())

max_values=[]
def multiply3(lst):
    prod=1
    for i in lst:
        prod=prod*i
    return prod

for combis in permutations(lst,3):
    #print(combis)
    n=multiply3(combis)
    max_values.append(n)

print(max(max_values))



