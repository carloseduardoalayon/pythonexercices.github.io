print("************************************************")
print("Sistema para reconocer que numero es mas grande")
print("************************************************\n ")

nu = int(input("Por favor, ingrese el primer numero: "))
nd = int(input("Por favor, ingrese el segundo numero: "))
nt = int(input("Por favor, ingrese el tercer numero: "))

if nu > nd and nu > nt:
    print("El numero ", nu, "es el mas grande. ")

elif nd > nt:
    print("El numero ", nd, "es el mas grande. ")

else:
    print("El numero ", nt, "es el mas grande. ")
