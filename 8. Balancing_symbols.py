def is_balanced(expression):
    stack = []
    matching = {')':'(', ']':'[', '}':'{'}

    for char in expression:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack.pop() != matching[char]:
                return False

    return len(stack)==0

expression = input()
result = is_balanced(expression)
if result == True:
    print("The given expression is balanced")
else:
    print("The given expression is not balanced")