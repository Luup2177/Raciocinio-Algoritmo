Cel = float(input("Temp Celsius: "))
choice = input("Conversão para Fahrenheit (F) ou Kelvin (K) ?").upper()
if choice == "F":
    Fahrenheit = (Cel * 9 /5) + 32
    print(f"{Cel}ºC = {Fahrenheit}ºF")
elif choice == "K":
    Kelvin = Cel + 273.15
    print(f"{Cel}ºC = {Kelvin}K")
else :
    print("Resultado desconhecido . Por favor escolha F para Fahrenheit ou K para Kelvin")