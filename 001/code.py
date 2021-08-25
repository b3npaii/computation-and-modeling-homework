def sum_of_n_numbers(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


def word_symmetry(word):
    if word == word[::-1]:
        return "True"
    else:
        return "False"


def convert_to_numbers(input_string):
    new_arr = []
    alph = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in input_string:
        if letter in alph:
            new_arr.append(alph.index(letter))
    return new_arr


def is_prime(n):
    for m in range(2, n//2):
        if n % m == 0:
            return "False"
        else:
            return "True"


