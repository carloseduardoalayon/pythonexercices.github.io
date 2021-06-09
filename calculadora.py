print("***********")
print("Calculadora")
print("***********\n")


print(" 1: Suma \n 2: Resta \n 3: Multiplicacion \n 4: Division \n 5: Div Entera \n 6: Exponencial \n 7: Resto \n ")

numero = int(input("Selecciona la operacion que deseas realizar: "))

if numero == 1:
    print("Escogiste suma \n")
    numero = int(input("Introduce el primer numero: "))
    numero += int(input("Introduce el segundo numero: "))
    print("El resultdo es: ", numero)
    
elif numero == 2:
    print("Escogiste resta \n")
    numero = int(input("Introduce el primer numero: "))
    numero -= int(input("Introduce el segundo numero: "))
    print("El resultdo es: ", numero)
    
elif numero == 3:
    print("Escogiste multiplicacion \n")
    numero = int(input("Introduce el primer numero: "))
    numero *= int(input("Introduce el segundo numero: "))
    print("El resultdo es: ", numero)

elif numero == 4:
    print("Escogiste division \n")
    numero = float(input("Introduce el primer numero: "))
    numero /= float(input("Introduce el segundo numero: "))
    print("El resultdo de la division es: ", round(numero, 2))

elif numero == 5:
    print("Escogiste Division entera \n")
    numero = int(input("Introduce el primer numero: "))
    numero //= int(input("Introduce el segundo numero: "))
    print("El resultado de la division entera es: ", numero)

elif numero == 6:
    print("Escogiste exponente \n")
    numero = int(input("Introduce el primer numero: "))
    numero **= int(input("Introduce el segundo numero: "))
    print("El exponent es: ", numero)

elif numero == 7:
    print("Escogiste modulo o resto \n")
    numero = int(input("Introduce el primer numero: "))
    numero %= int(input("Introduce el segundo numero: "))
    print("El modulo o resto es: ", numero)

else:
    print("Esta opcion no existe.")


