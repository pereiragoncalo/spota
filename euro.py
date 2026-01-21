import random

# Gerar a chave do Totoloto (5 números únicos entre 1 e 49)
chave = random.sample(range(1, 50), 5)

# Lista para guardar os números do utilizador
aposta = []

print("Bem-vindo ao Totoloto!")
print("Tente adivinhar 5 números entre 1 e 49 (sem repetir).")

# Pedir os 5 números ao utilizador
while len(aposta) < 5:
    numero = int(input(f"Introduza o {len(aposta) + 1}º número: "))

    if numero < 1 or numero > 49:
        print("Número inválido. Deve ser entre 1 e 49.")
    elif numero in aposta:
        print("Número repetido. Escolha outro.")
    else:
        aposta.append(numero)

# Verificar quantos números acertou
acertos = 0
for num in aposta:
    if num in chave:
        acertos += 1

# Mostrar resultados
print("\nA sua aposta:", aposta)
print("Chave vencedora:", chave)
print(f"Acertou em {acertos} número(s).")