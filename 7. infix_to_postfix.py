def infix_to_postfix(expression):
    precednce = {'(':0, '+':1, '-':1, '*':2, '/':2, '^':3 }

    output = []
    stack = []

    for char in expression.split():
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while (stack and precednce[stack[-1]] >= precednce[char]):
                output.append(stack.pop())
            stack.append(char)


    while stack:
        output.append(stack.pop())

    return ' '.join(output)

expression = "( A + B ) * C - ( D / E )"
print(infix_to_postfix(expression))