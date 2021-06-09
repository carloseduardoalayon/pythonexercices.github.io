print("Sistema para calcular el promedio de un alumno")

nombre = input("Para comenzar,¿Cual es tu nombre?: ")


matematicas = float(input(nombre + ": ¿Cual es tu calificacion de matematicas?: "))
quimica = float(input(nombre + ": ¿Cual es tu calificacion de quimica?: "))
biologia = float(input(nombre + ": ¿Cual es tu calificacion de biologia?: "))

promedio = ( matematicas + quimica + biologia ) / 3

if promedio  >= 6:
    print('Felicidades ' + nombre + ' "Aprobaste" con un promedio de: ', promedio)
    print('Felicidades ' + nombre + ' "Aprobaste" con un promedio de: ', round(promedio, 2))
    
else:
    print('Lo sentimos' + nombre + ' "Reprobaste" con un promedio de:', promedio)
    print('Lo sentimos' + nombre + ' "Reprobaste" con un promedio de:', round(promedio, 2))
    
print("Fin")    







print("Condicional_compuesta")

numero_uno = 5

if numero_uno == 5 :
    print("El numero es cinco.")

else:
    print("El numero No es cinco.")

print("Fin.") 
