import random

numero_min = int(input("Digite o valor mínimo "))
numero_max = int(input("Digite o valor máximo "))

numero_pc = random.randint(numero_min, numero_max)

print(f"Escolha um valor entre {numero_min} e {numero_max}")

tentativas = 0

while tentativas <=20:
    tentativas += 1
    escolha = int(input("Aposte um Valor : "))
    if numero_pc == escolha:
        print(f"Parabens você acertou o Valor {numero_pc}")
        break
    elif escolha < numero_pc:
        print("Número escolhido pela máquina foi Superior")
    elif escolha > numero_pc:
        print("Número escolhido pela máquina foi Inferior")
    
    if tentativas == 20:
        print(f"Suas chances se esgotaram\n infelizmente você não conseguiu acertar o Valor {numero_pc}  ")
        break
