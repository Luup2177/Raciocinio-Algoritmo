def media(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

print(media([1, 2, 3, 4, 5]))
print(media([10, 20, 30,40,50]))
print(media([]))
help(media)
