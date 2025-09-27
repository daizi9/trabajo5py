#Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
último pasa a ser el primero.

numeros = [1, 2, 4, 40, 8, 14, 70]

# Guardar el último elemento
ultimo = numeros.pop()
# Insertarlo al principio
numeros.insert(0, ultimo)

print("Lista rotada una posición a la derecha:", numeros)
