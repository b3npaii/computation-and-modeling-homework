from code import encode
from code import decode
from code import brute_force_decode
from code import bisection_search
from code import Stack
from code import Queue
from code import calc_minimum
from code import simple_sort

if decode(encode("what", 3, 4), 3, 4) == "what":
    print("decode and encode are working")
if encode(decode([7, 13, 19], 6, 1), 6, 1) == [7, 13, 19]:
    print("decode and encode are working")

print(brute_force_decode([377, 717, 71, 513, 105, 921, 581, 547, 547, 105, 377, 717, 241, 71, 105, 547, 71, 377, 547, 717, 751, 683, 785, 513, 241, 547, 751], 101, 101))

print(bisection_search(14, 2, 3, 3))
print(bisection_search(9, 2, 4, 2))
print(bisection_search(7, 2, 3, 2))

stacks = Stack()
stacks.push("what")
stacks.push("is")
stacks.push("this")
stacks.print()
stacks.pop()
stacks.print()

lists = Queue()
lists.enqueue("thing 1")
lists.enqueue("thing 2")
lists.enqueue("thing 3")
lists.print()
lists.enqueue("thing 4")
lists.print()
lists.dequeue()
lists.print()

if calc_minimum([1, 2, 3, -1, 1]) == -1:
    print("calc_minimum is working")
if calc_minimum([0, 1, 2, 3, 17]) == 0:
    print("calc_minimum is working")

if simple_sort([1, 15, 7, -1]) == [-1, 1, 7, 15]:
    print("simple_sort is working")
print(simple_sort([1, 2, 3, 7, 0, -5, -2]))