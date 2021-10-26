from code import merge_sort

a = [5, 8, 1, 4, 9, -3, 0.5, 0, 5]
if merge_sort(a) != [-3, 0, 0.5, 1, 4, 5, 5, 8, 9]:
    print("false 1")
b = [-1, -1, -3, 8, 0]
if merge_sort(b) != [-3, -1, -1, 0, 8]:
    print("false 2")
c = [7, 3, 4.5, 9, 0]
if merge_sort(c) != [0, 3, 4.5, 7, 9]:
    print("false 3")