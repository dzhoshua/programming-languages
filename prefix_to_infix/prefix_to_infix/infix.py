def to_infix(expr):
    operators = ['+', '-', '*', '/']
    simbols = expr.split()
    infix_expr=[]

    for s in reversed(simbols):
        if s.isdigit():
            infix_expr.append(s)
        elif s in operators:
            if len(infix_expr) < 2:
                raise ValueError("Недостаточно чисел для перевода в инфиксную запись.")
            number1 = infix_expr.pop()
            number2 = infix_expr.pop()
            infix_expr.append(f'({number1} {s} {number2})')
        else:
            raise TypeError(f"Неизвестный символ '{s}'. Используйте только бинарные операторы и беззнаковые числа.")
        
    if len(infix_expr) < 1:
        raise ValueError("Вы отправили пустую строку")
    
    return infix_expr[0]