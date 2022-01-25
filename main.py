#Resursion
def recursive_factorial(n):
    if n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)

num = int(input("Number: "))

if num < 0:
    print("Number too low!")
elif num == 0:
    print("0! = 0")
else:
    print(f"{num}! = {recursive_factorial(num)}")