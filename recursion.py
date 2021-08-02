#RECURSION

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

print(fact(5))


#Write a recursive python function that returns the sum of first n integers
#HINT: The function will be similar to the factorial function

def sum(n):
    if n<=1:
        return n
    else:
        return n+sum(n-1)

print(sum(2))
