from code import word_symmetry
from code import sum_of_n_numbers
from code import convert_to_numbers
from code import is_prime

if word_symmetry("thing") == "True":
    print("word_symmetry is not working")
if word_symmetry("taddat") == "True":
    print("word_symmetry is working")
if is_prime(20) == "False":
    print("is_prime is working")
if convert_to_numbers("abc") != [1, 2, 3]:
    print("convert_to_numbers is not working")
if convert_to_numbers("abc") == [1, 2, 3]:
    print("convert_to_numbers is working")
if sum_of_n_numbers(10) != 55:
    print("sum_of_n_numbers is not working")
if sum_of_n_numbers(10) == 55:
    print("sum_of_n_numbers is working")
