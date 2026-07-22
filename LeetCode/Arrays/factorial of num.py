def factorial(n):
    if n==0:
        return 1
    if n==1:
        return 1

    fact=factorial(n-1)*n

    return fact


print(factorial(5))