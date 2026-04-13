import os
def centro(texto):
    print(texto.center(100))

# Valor inicial dos contadores
excelente = 0
ruim = 0

# Número de entrevistados
total_entrevistados = 50

for i in range(total_entrevistados):
    print(f"\nEntrevistado: {i + 1}")

    nome = input("Digite o nome: ")

    while True:
        try:
            idade = int(input("Digite a idade: "))
            if idade <= 0 or idade >= 120:
                print("Idade inválida! Digite um número maior que 0 e menor que 120.")
                continue
            break  # só sai se for válido
        except ValueError:
            print("Idade inválida! Digite um número.")

    print("Opinião sobre o atendimento: \n1 - EXCELENTE  \n2 - BOM  \n3 - RUIM")
    opiniao = int(input("Digite a opção (1, 2 ou 3): "))
    os.system('cls' if os.name == 'nt' else 'clear')

    # Estrutura de decisão
    if opiniao == 1:
     excelente += 1
    elif opiniao == 2:
        pass  # Não contabiliza, apenas ignora
    elif opiniao == 3:
        ruim += 1
    else:
        print("Opção inválida! Resposta não foi contabilizada pelo sistema.")

# Exibição dos resultados
centro("=== RESULTADO DA PESQUISA ===")
centro(f"Quantidade de respostas EXCELENTE: {excelente}")
centro(f"Quantidade de respostas RUIM: {ruim}")
