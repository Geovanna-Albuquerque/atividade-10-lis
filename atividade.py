#Faça um programa que leia um número
indeterminado de notas. Após esta entrada de
dados, faça o seguinte:
• Mostre a quantidade de notas que foram lidas.
• Exiba todas as notas na ordem em que foram
informadas.
• Exiba todas as notas na ordem inversa à que
foram informadas, uma abaixo do outra.
• Calcule e mostre a soma das notas.
• Calcule e mostre a média das notas.
• Calcule e mostre a quantidade de notas acima
da média calculada.

# Lista para armazenar as notas
notas = []

# Loop para ler as notas até o usuário informar uma nota negativa
while True:
    nota = float(input("Digite uma nota (ou uma nota negativa para sair): "))
    
    if nota < 0:
        break
    
    # Adiciona a nota à lista
    notas.append(nota)

# Quantidade de notas lidas
quantidade_notas = len(notas)
print(f"Quantidade de notas lidas: {quantidade_notas}")

# Exibe todas as notas na ordem em que foram informadas
print("Notas na ordem informada:")
for nota in notas:
    print(nota)

# Exibe todas as notas na ordem inversa
print("Notas na ordem inversa:")
for nota in reversed(notas):
    print(nota)

# Calcula a soma das notas
soma_notas = sum(notas)
print(f"Soma das notas: {soma_notas}")

# Calcula a média das notas
if quantidade_notas > 0:
    media_notas = soma_notas / quantidade_notas
    print(f"Média das notas: {media_notas:.2f}")
    
    # Calcula a quantidade de notas acima da média
    acima_da_media = sum(1 for nota in notas if nota > media_notas)
    print(f"Quantidade de notas acima da média: {acima_da_media}")
else:
    print("Não foram informadas notas suficientes.")

