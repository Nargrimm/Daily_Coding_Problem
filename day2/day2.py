'''
Given an array of integers, return a new array 
such that each element at index i of the new array is the product 
of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5],
the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
'''

def array_product(l):
  product = 1
  for i in l:
    product *= i
  for i in range(len(l)):
    l[i] = product / l[i]
  return l

if (array_product([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]):
  print("OK")
else:
  print("KO")
if (array_product([3, 2, 1]) == [2, 3, 6]):
  print("OK")
else:
  print("KO")