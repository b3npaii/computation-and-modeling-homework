from code import word_symmetry
from code import sum_of_n_numbers
from code import convert_to_numbers
from code import is_prime
from code import get_intersection
from code import get_union
from code import count_characters
from code import get_first_n_terms_nonrecursive
from code import get_n_term_recursive
from code import convert_to_base_10
from code import nth_fibonacci_number
from code import convert_to_base_2


if word_symmetry("thing") == True:
    print("word_symmetry is not working")

if word_symmetry("!taddat!") == True:
    print("word_symmetry is working")

if is_prime(20) == False:
    print("is_prime is working")

if is_prime(23) == True:
    print("is_prime is working")

if convert_to_numbers("abc") != [1, 2, 3]:
    print("convert_to_numbers is not working")

if convert_to_numbers(" qwe") == [0, 17, 5]:
    print("convert_to_numbers is working")

if sum_of_n_numbers(500) == 125250:
    print("sum_of_n_numbers is working")

if sum_of_n_numbers(10) == 55:
    print("sum_of_n_numbers is working")

if get_intersection([1, 2, 3, 4, 5], [4, 5, 6]) == [4, 5]:
    print("get_intersection is working")

if get_intersection(["abc", 4, "17"], ["abc", 8, "jk"]) == ["abc"]:
    print("get_intersection is working")

if get_union([1, 2, 3, 4, 5], [45, 6, 7, 5]) == [1, 2, 3, 4, 5, 45, 6, 7]:
    print("get_union is working")

if get_union([1, 2, 3, "abc1"], [7, "abc1"]) == [1, 2, 3, "abc1", 7]:
    print("get_union is working")

array = get_first_n_terms_nonrecursive(6)

if array[5] != get_n_term_recursive(6):
    print("broke")
else:
    print("work")

if get_first_n_terms_nonrecursive(3) == [5, 11, 29]:
    print("get_first_n_terms_nonrecursive is working")

if get_n_term_recursive(3) == 29:
    print("get_n_term_recursive is wokring")

if convert_to_base_10(convert_to_base_2(10)) != 10:
    print("one of the conversions is broke")
else:
    print("conversions are working")

if convert_to_base_2(convert_to_base_10(10110)) != 10110:
    print("conversions are not wokring")
else:
    print("conversions are working")
