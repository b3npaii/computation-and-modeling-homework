from code import swap_sort
from code import tally_sort
from code import card_sort

if swap_sort([-1, 7, 0, 1.1, 7, 9]) != [-1, 0, 1.1, 7, 7, 9]:
    print("swap_sort is broke")
if swap_sort([1, 2, 7, -1, 9]) != [-1, 1, 2, 7, 9]:
    print("swap_sort is broke")
if tally_sort([0, -1, 4, 7.2, 9, -11, -1]) != [-11, -1, -1, 0, 4, 7, 9]:
    print("tally_sort is broke")
if tally_sort([0, 2, 5, -9, -7]) != [-9, -7, 0, 2, 5]:
    print("tally_sort is broke")
if card_sort([9, 8, 4, 6, -1.2, 0, 5, 5]) != [-1.2, 0, 4, 5, 5, 6, 8, 9]:
    print("card_sort is broke")
if card_sort([0, 1, 5, -3, 9.1]) != [-3, 0, 1, 5, 9.1]:
    print("card_sort is broke")