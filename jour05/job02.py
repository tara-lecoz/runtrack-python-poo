def puissance(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return puissance(x, n//2) ** 2
    else:
        return x * puissance(x, n-1)

x = int(input("Entrez un nombre : "))
n = int(input("Entrez un entier : "))
print(x, "^", n, "=", puissance(x, n))