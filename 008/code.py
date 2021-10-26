def merge(x, y):
    x_index = 0
    y_index = 0
    answer = []
    while (len(x) + len(y)) > len(answer):
        if x_index == len(x):
            for i in range(y_index, len(y)):
                answer.append(y[i])
        elif y_index == len(y):
            for i in range(x_index, len(x)):
                answer.append(x[i])
        elif x[x_index] < y[y_index]:
            answer.append(x[x_index])
            x_index += 1
        elif y[y_index] < x[x_index]:
            answer.append(y[y_index])
            y_index += 1
        elif y[y_index] == x[x_index]:
            answer.append(x[x_index])
            x_index += 1
    return answer

def divide_list(input):
    front = []
    back = []
    for i in range(0, len(input)):
        if i < int(len(input) / 2):
            front.append(input[i])
        else:
            back.append(input[i])
    return front, back

def merge_sort(input):
    if len(input) > 1:
        front, back = divide_list(input)
        sorted_front = merge_sort(front)
        sorted_back = merge_sort(back)
        return merge(sorted_front, sorted_back)
    else:
        return input
