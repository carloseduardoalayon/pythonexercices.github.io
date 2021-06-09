print("Sistema para calcular el promedio de un alumno")

nombre = input("Para comenzar, ¿cual es tu nombre?: ")
matematicas = int(input(nombre + " ¿Cual es tu calificacion en matemáticas: "))
quimica = int(input(nombre + " ¿Cual es tu calificacion en química: "))
biologia = int(input(nombre + " ¿Cual es tu calificacion en biología: "))

promedio = (matematicas + quimica + biologia) / 3
promedio = int(promedio)

if promedio >= 6:
    print('Felicidades ' + nombre + ' "Aprobaste" ' + 'Con un promedio de: ', promedio)


print("Fin.")

