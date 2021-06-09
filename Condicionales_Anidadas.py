print("===========")
print("Conversor")
print("=========== \n")


print("Menu de opciones: \n")
print("Presiona 1 para convertir de numero a palabra.")
print("Presiona 2 para convertir de palabra a número. \n")

opcion = int(input("¿Cual es tu opcion deseada:"))

if opcion == 1:
    print("\n Conversor de numero a palabra. \n")

    opcion_uno = int(input("¿Cual es el numero que deseas convertir a palabra?: "))

    if opcion_uno == 1:
        print("El numero es 'UNO'")

    elif opcion_uno == 2:
        print("El numero es 'DOS'")

    elif opcion_uno == 3:
        print("El numero es 'TRES'")

    elif opcion_uno == 4:
        print("El numero es 'Cuatro'")

    elif opcion_uno == 5:
        print("El numero es 'Cinco'")

    else:
        print("El numero seleccionado no esta registrado.")

        
        

elif opcion == 2:
    print("\n Conversor de palabra a numero. \n")

    opcion_dos = input("Cual es la palabra que deseas convertir a número?:")
    opcion_dos = opcion_dos.lower()

    if opcion_dos == "uno":
        print("el numero es '1.'")

    elif opcion_dos == "dos":
        print("el numero es '2'")

    elif opcion_dos == "tres":
        print("el numero es '3'")

    elif opcion_dos == "cuatro":
        print("el numero es '4'")

    elif opcion_dos == "cinco":
        print("el numero es '5'")    

    else:
        print("El numero seleccionado no esta registrado. ")
            
else:
    print("Opción no disponible.")

print ("Fin.")
