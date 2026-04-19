#+ is addition -is subtraction * is multiplication / is division
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

    
