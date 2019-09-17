'''
Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''

def get_all_permutations(l):
  if len(l) == 2:
    return ([l, [l[1], l[0]]])
  else:
    res = []
    for pos, item in enumerate(l):
      tmp = list(l)
      fixed = tmp.pop(pos)
      for elem in get_all_permutations(tmp):
        res += [[fixed] + elem] 
    return res

print(get_all_permutations([1, 2, 3, 4]))