#Lista con valores repetidos
datos=[1,3,5,3,7,1,9,5,3]

#Usamos set para eliminar duplicados y luego convirtiendo a lista
sin_repetir =list(set(datos))

print("Lista original:", datos)
print("Lista sin elementos repetidos", sin_repetir)