from copy import deepcopy
a = [[0,0,0],[1,1,1],[2,2,2]]
b = deepcopy(a)
print(a)
print(b)
a[0][0] = 1
print(a)
print(a == b)
print(b)