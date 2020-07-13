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
    math_expression = ''
    for i in range(9):
        math_expression += f'{9-i}{mark[i]}'
    math_expression += '0'
    return math_expression


def pro_solution(expected_result):
    dict_results = {}
    quantity = 3**9
    for i in range(quantity):
        expression = math_expression(i)
        result = eval(expression)
        if result in dict_results:
            dict_results[result].append(expression)
        else:
            dict_results[result] = [expression]
    if expected_result in dict_results:
        return f'Результат {expected_result} дают выражения {dict_results[expected_result]}'
    else:
        return f'К сожалению не существует выражения, результатом которого являлось бы число {expected_result}.'


print(pro_solution(200))
