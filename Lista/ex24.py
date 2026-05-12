def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

print(fatorial(5))
print(fatorial(0))
print(fatorial(7))
print(fatorial(10))