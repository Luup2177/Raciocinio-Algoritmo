def par_ou_impar(num):
    if num % 2 == 0:
        print(num," é par ")
        return num
    else:
        print(num," é impar")
        return num
resultado = par_ou_impar(10)
print(resultado)
