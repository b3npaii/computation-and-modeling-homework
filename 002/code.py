def encode(string, a, b):
    arr = []
    alph = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in string:
        if letter in alph:
            arr.append(a*alph.index(letter) + b)
    return arr


def decode(numbers, a, b):
    answer = ""
    alph = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for number in numbers:
        guess1 = number - b
        guess2 = guess1 / a
        if guess2 in range(53):
            answer += alph[int(guess2)]
        elif guess2 not in range(0, 53):
            break
    return answer


def brute_force_decode(numbers, bound_one, bound_two):
    alph = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(0, bound_one):
        for j in range(0, bound_two):
            answer = []
            for part in numbers:
                part = part - j
                if part < 0:
                    break
                if i != 0:
                    part = part / i
                    if part > 52:
                        break
                    elif part % 1 != 0:
                        break
                    else:
                        answer.append(alph[int(part)])
                else:
                    break
            else:
                print("".join(answer))


def bisection_search(num, lower_bound, upper_bound, root):
    while (upper_bound - lower_bound > 0.000000000000001):
        approximation = (lower_bound + upper_bound)/2
        if approximation ** root == num:
            return approximation
        if approximation ** root < num:
            lower_bound = (lower_bound + upper_bound) / 2
        if approximation ** root > num:
            upper_bound = (lower_bound + upper_bound) / 2
    return approximation


class Stack:
    def __init__(self):
        self.data = []

    def print(self):
        reversed = self.data[::-1]
        for i in reversed:
            print(i)

    def push(self, element):
        self.data.append(element)

    def pop(self):
        self.data.pop(len(self.data) - 1)


class Queue:
    def __init__(self):
        self.line = []

    def print(self):
        for i in self.line:
            print(i)

    def enqueue(self, item):
        self.line.append(item)

    def dequeue(self):
        self.line.remove(self.line[0])
        return self.line[0]


def calc_minimum(numbers):
    a = numbers[0]
    for number in numbers:
        if number < a:
            a = number
    return a


def simple_sort(numbers):
    answer_arr = []
    for number in numbers:
        while len(numbers) > 0:
            value = calc_minimum(numbers)
            answer_arr.append(value)
            numbers.remove(value)
    return answer_arr
