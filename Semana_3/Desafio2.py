numeros = (2, 5, 8, 9, 12, 15, 18)

print("Números menores de 15:")
for n in numeros:
    if n <= 15:
        print(n, end=' ')
print()  

contagem = 0
for n in numeros:
    if n <= 15 and n % 2 == 0:
        contagem += 1

print("Quantidade de números pares =", contagem)

