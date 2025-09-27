#Crear una matriz con las notas de 5 estudiantes en 3 materias.
• Mostrar el promedio de cada estudiante.
• Mostrar el promedio de cada materia.

notas = [
    [7, 8, 6],  # Estudiante 1
    [9, 7, 7],  # Estudiante 2
    [8, 9, 10], # Estudiante 3
    [6, 8, 8],  # Estudiante 4
    [8, 7, 10]   # Estudiante 5
]

#Promedio de cada uno
for i, estudiante in enumerate(notas, 1):
    promedio = sum(estudiante) / len(estudiante)
    print(f"Promedio estudiante {i}: {promedio:.2f}")

#Promedio de cada estudfiante en cada materia
num_materias = len(notas[0])
for j in range(num_materias):
    suma_materia = 0
    for i in range(len(notas)):
        suma_materia += notas[i][j]
    promedio_materia = suma_materia / len(notas)
    print(f"Promedio materia {j+1}: {promedio_materia:.2f}")