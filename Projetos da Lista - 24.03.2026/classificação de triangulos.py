l1= float(input("Lado 1: "))
l2= float(input("Lado 2: "))
l3= float(input("Lado 3: "))

if l1 == l2 == l3:
    print("Equilátero")
elif l1 == l2 or l2 == l3 or l1 == l3:
    print("Isósceles")
else:
    print("Escaleno")