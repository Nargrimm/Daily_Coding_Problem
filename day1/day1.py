
'''
Problem #1 Easy
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''


def sum_in_list_dummy(k, l):
  start = 0
  while start < len(l):
    remaining = k
    remaining -= l[start]
    for i in l[start:]:
      if remaining == i:
        return True
    start += 1
  return False


'''
  Bonus: Can you do this in one pass?
    -> We can do it in one pass if the array is sorted.
    -> We iterate from the beginning and the end moving accordingly if we need to increase or decrase the value
'''


def sum_in_list_bonus(k, l):
  l.sort()
  start = 0
  end = len(l) - 1
  while end > start:
    if l[start] + l[end] == k:
      return True
    elif l[start] + l[end] < k:
      start += 1
    else:
      end -= 1
  return False


print(sum_in_list_dummy(17, [10, 15, 3, 7]))
print(sum_in_list_dummy(19, [11, 15, 3, 10, 4]))
print(sum_in_list_dummy(19, [11, 12, 3, 10, 4]))

print(sum_in_list_bonus(17, [10, 15, 3, 7]))
print(sum_in_list_bonus(19, [11, 15, 3, 10, 4]))
print(sum_in_list_bonus(19, [11, 12, 3, 10, 4]))
print(sum_in_list_bonus(45, [11, 12, 3, 10, 4, 15, 19, 23, 22]))
print(sum_in_list_bonus(45, [11, 12, 3, 10, 4, 15, 19, 23, 21]))
