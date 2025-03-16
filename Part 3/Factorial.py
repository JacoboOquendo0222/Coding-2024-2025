def factorial(numberline):
    for i in range(1,numberline):
        numberline*=i
    return numberline
def factorial2(number):
    if number==0:
        return 1
    else:
        return number*factorial2(number-1)
print("What is your number.")
number=int(input())
print("The factorial of the number is", factorial2(number))