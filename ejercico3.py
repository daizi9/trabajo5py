#Crear lista con nombre de 8 estudiantes presentes en clase


numeros = []
for in range (15);
    numero = int(input(f"Ingrese el numero {i+1}"))
    numeros.append(numero)

pares = []
impares = []

for num in numeros:
    if num%2 ==0:
        pares.append(num)
    else:
        impares.append(num)

print("Ingreso los numeros:", numeros)
print("Cantidad de pares:", len(pares))
print("Cantidad de impared:", len(impares))