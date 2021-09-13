def calc_minimum(numbers):
    a = numbers[0]
    for number in numbers:
        if number < a:
            a = number
    return a


def calc_maximum(numbers):
    a = numbers[0]
    for number in numbers:
        if number > a:
            a = number
    return a


def check_if_sorted(numbers):
    for number in numbers:
        if number > numbers[numbers.index(number) + 1]:
            return False


def swap_left(numbers, i, j):
    numbers[i], numbers[j] = numbers[j], numbers[i]


def swap_sort(numbers):
    for number in numbers:
        for i in range(0, len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    return numbers


def tally_sort(numbers):
    minimum = calc_minimum(numbers)
    shifted = []
    maximum = calc_maximum(numbers)
    tallies = []
    answer = []
    for number in numbers:
        shifted.append(number - minimum)
    for i in range(0, round(calc_maximum(shifted) + 1)):
        tallies.append(0)
    for number in shifted:
        tallies[round(number)] += 1
    for i, number in enumerate(tallies):
        for j in range(0, number):
            answer.append(i + minimum)
    return answer


def card_sort(numbers):
    for number in numbers:
        for i in range(0, len(numbers)):
            if i > 0:
                while numbers[i] < numbers[i - 1]:
                    numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]
    return numbers
