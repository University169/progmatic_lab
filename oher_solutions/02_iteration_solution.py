def ternary(num):
    base = 3
    res = ''
    while num > 0:
        res = str(num % base) + res
        num //= base
    return res


def math_expression(k):
    ter = ternary(k)
    ter_list = list(ter)
    mark = [''] * 9
    for i in range(1, 10):
        t = i - 1
        i *= (-1)
        if t < len(ter_list):
            element = int(ter_list[i])
            if element == 0:
                mark[i] = ''
            elif element == 1:
                mark[i] = '+'
            elif element == 2:
                mark[i] = '-'
        else:
            mark[i] = ''
    result = ''
    for i in range(9):
        result += f'{9-i}{mark[i]}'
    result += '0'
    return result


def simple_solution(expected_result):
    for i in range(3 ** 9):
        expression = math_expression(i)
        if eval(expression) == expected_result:
            return f'Результат {expected_result} дает выражение {expression}.'
    return f'К сожаление не существует выражения, результатом которого являлось бы число {expected_result}.'


print(simple_solution(200))
# данное выражение 2778 по счету
