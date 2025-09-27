#Lista con la nota de 10 estudiantes
 
notas =  [7, 8.5, 6, 9, 10, 5.5, 7.5, 8, 6.5, 9.5]

#Mostrar la lista
for i, nota in enumerate (notas, 1):
    print(f"Estudiante{i}: {nota}")

#Calcular promedio

promedio = sum(notas) / len(notas)
print(f"Promedio de notas: {promedio: .2f}")

#La nota mas alta y baja
print (f"Nota mas alta: {max(notas)}")
print(f"Nota mas baja: {min(notas)}")

