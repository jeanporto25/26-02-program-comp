numero1 = 25
numero2 = 30 
soma = numero1 + numero2
print("a soma dos numeros e", soma)


n = 5
fatorial = 1

for i in range(1, n + 1):
    fatorial *= i

print(f"O fatorial de {n} é {fatorial}")


for i in range(10, 0, -1):
    print(i)



numero = 20

if numero % 3 == 0 and numero % 5 == 0:
    print(f"O número {numero} é múltiplo de 3 e 5 ao mesmo tempo.")
else:
    print(f"O número {numero} não é múltiplo de 3 e 5 ao mesmo tempo.")