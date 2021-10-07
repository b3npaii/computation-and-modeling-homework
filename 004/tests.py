from code import merge
from code import newton_rhapson

if merge([1, 5, 7, 11, 19], [2, 3, 4]) != [1, 2, 3, 4, 5, 7, 11, 19]:
    print("merge is broken")
if merge([-12, 1, 2.3], [1, 2.3, 7, 12]) != [-12, 1, 1, 2.3, 2.3, 7, 12]:
    print("merge is broken")
print("The square root of two, with precision of 6, is approximately")
print(newton_rhapson(2, 2, 6))
print("The actual square root of 2 is")
print(2 ** (1/2))
print("The cube root of seven, with precision of 8, is approximately")
print(newton_rhapson(7, 3, 8))
print("The actual cube root of 7 is")
print(7 ** (1/3))