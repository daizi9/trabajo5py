#Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7

ventas = [
    [10, 12, 9, 15, 11, 10, 13],  #Producto1
    [5, 7, 6, 8, 7, 6, 5],        #Producto2
    [20, 18, 22, 19, 21, 20, 23], #Producto3
    [8, 9, 7, 3, 14, 9, 8]       #Prroducto4
]

#Total vendido por productos

for i,producto in enumerate (ventas, 1):
    total=sum(producto)
    print(f"Toal vendido por producto {i}: {total}")

#Ttotal de ventas por dia (sumar columnas)
ventas_pordia = []
for dia in range(7):
 total_dia = sum(ventas[prod][dia] for prod in range(4))
    ventas_por_dia.append(total_dia)