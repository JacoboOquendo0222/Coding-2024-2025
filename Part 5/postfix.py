#+ is addition -is subtraction * is multiplication / is division
from Stack import Stack
def isoperator(listis):
    if listis=="+":
        return True
    if listis=="-":
        return True
    if listis=="*":
        return True
    if listis=="/":
        return True
    return False
def evaluate(one,two,operator):
    if operator=="+":
        return one+two
    if operator=="-":
        return one-two
    if operator=="*":
        return one*two
    if operator=="/":
        return one/two
def parse(expression):
    tokens=expression.split()
    stack=Stack()
    for token in tokens:
        if isoperator(token):
            two=stack.pop()
            one=stack.pop()
            result=evaluate(one,two,token)
            stack.push(result)
        else:
            stack.push(float(token))
    return stack.pop()
print(parse("1 1 + 2 2 + + 5 /"))