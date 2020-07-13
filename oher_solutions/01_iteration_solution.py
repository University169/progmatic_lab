def ternary(num): # переводим число в троичную
    base = 3
    res = ''
    while num > 0:
        res = str(num % base) + res
        num //= base
    return res # обращаю внимание, что возвращается строка !!


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
    # math_expression = f'9{mark[0]}8{mark[1]}7{mark[2]}6{mark[3]}5{mark[4]}4{mark[5]}3{mark[6]}2{mark[7]}1{mark[8]}0'
    return math_expression


a = []
dict_results = {}
print(f'Переберем {3**9} возможных математических выражений.')
quantity = 3**9
for i in range(quantity):
    expression = math_expression(i)
    result = eval(expression)
    dict_results[result] = expression
print(f'Количество возможных различных значений = {len(dict_results)}.')
expected_result = int(input('Укажите ожидаемый результат: ')) # можно подставить любое значение
if expected_result in dict_results:
    print(f'Результат {expected_result} дает выражение {dict_results[expected_result]}')
else:
    print(f'К сожаление не существует выражения, результатом которого являлось бы число {expected_result}.')


# -----------------------------------------
# Идея в том, что 9876543210 - это 10 цифр, между которыми 9 промежутков.
# в каждом промежутке может быть вставлен  +, - или ничего
# скобки не предполагаются, значит всего возможных вариантов 3**9 = 19683

# просто составим словарь, в котором каждому возможному результату сопоставлен список из всех подходящих выражений
