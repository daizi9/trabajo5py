#Lista de 5 productos

productos[]

for i in range (5):
    producto= input (f"Ingrese el nombre del producto {i+1}")
    productos.append(producto)


#Mostramos la lista ordenada alfabeticamente usando sorted ()
productos_ordenados = sorted(productos)
for p in productos_ordenados:
    print(p)

#Pedimos al usuario el nombre del producto que desea eliminar

eliminar= input("Ingrese el nombre del producto que desea eliminar:")
if eliminar in productos:
    productos.remove(eliminar)
else:
    print("Se actualizo su lista de productos:")
    for p in productos:
        print(p)