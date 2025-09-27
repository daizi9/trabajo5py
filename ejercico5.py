estudiantes = ["Ana", "Luis", "María", "Juan", "Sofía", "Carlos", "Marta", "Diego"]

accion = input("¿Desea agregar (z) o eliminar (o) un estudiante? (a/e): ").lower()

if accion == 'z':
    nuevo = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
elif accion == 'o':
    eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
    else:
        print("Estudiante no encontrado.")
else:
    print("Opción no válida.")

print("Lista actualizada de estudiantes:")
for est in estudiantes:
    print(est)
