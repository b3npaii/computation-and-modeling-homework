def newton_rhapson(x, n, precision):
    x_old = x
    while precision > 0:
        f_of_x = (x_old ** n) - x
        f_prime = n * (x_old ** (n - 1))
        x_new = x_old - f_of_x/f_prime
        x_old = x_new
        precision -= 1
    return x_new


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
