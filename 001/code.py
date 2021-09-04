import math

def sum_of_n_numbers(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


def word_symmetry(word):
    if word == word[::-1]:
        return True
    else:
        return False


def convert_to_numbers(input_string):
    new_arr = []
    alph = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in input_string:
        if letter in alph:
            new_arr.append(alph.index(letter))
    return new_arr


def is_prime(n):
    for m in range(2, n//2 + 1):
        if n % m == 0:
            return False
        elif m == n//2:
            return True


def get_intersection(list1, list2):
    answer = []
    for element in list1:
        if element in list2:
            if element not in answer:
                answer.append(element)
    return answer


def get_union(list1, list2):
    answer_array = []
    for element in list1:
        answer_array.append(element)
    for element in list2:
        if element not in list1:
            answer_array.append(element)
    return answer_array


def count_characters(input_string):
    answer_dict = {}
    lowercase_string = input_string.lower()
    for letter in lowercase_string:
        answer_dict[str(letter)] = lowercase_string.count(letter)
    return answer_dict


def get_first_n_terms_nonrecursive(n):
    answer_array = []
    for i in range(1, n+1):
        if i == 1:
            answer_array.append(5)
            previous_term = 5
        else:
            previous_term = 3*previous_term - 4
            answer_array.append(previous_term)
    return answer_array


def get_n_term_recursive(n):
    if n == 1:
        return 5
    return(get_n_term_recursive(n-1)*3 - 4)


def convert_to_base_10(n):
    n_digit_count = len(str(n))
    string_n = str(n)
    reverse_n = string_n[::-1]
    output = 0
    for i in range(0, n_digit_count):
        output = output + int(reverse_n[i]) * 2**i
    return output


def nth_fibonacci_number(n): 
    if n == 0:
        return 0
    if n== 1:
        return 1
    return(nth_fibonacci_number(n-1)+nth_fibonacci_number(n-2))


def convert_to_base_2(n):
    exponent_list = []
    output = 0
    while n > 0:
        n_log_2_rounded = math.floor(math.log(n,2))
        exponent_list.append(n_log_2_rounded)
        n = n - 2**n_log_2_rounded
    for exponent in exponent_list: 
        output += 10**exponent
    return output
