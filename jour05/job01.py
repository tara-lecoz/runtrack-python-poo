def factorial(n):
    if n == 1:
        return 1 
    else:
        return n * factorial(n-1)

num = int(input("Saisir un nombre : "))
print(f"La factorielle de {num} est {factorial(num)}")