# Inicialização dos contadores
excelente = 0
bom = 0
ruim = 0

# Definindo quantidade de entrevistados
total_entrevistados = 10  # use 50 depois de testar

# Loop FOR para coletar dados
for i in range(total_entrevistados):
    print(f"\nEntrevistado {i+1}")
    
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    
    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    
    opiniao = int(input("Digite sua opinião (1, 2 ou 3): "))
    
    # Estrutura de decisão
    if opiniao == 1:
        excelente += 1
    elif opiniao == 2:
        bom += 1
    elif opiniao == 3:
        ruim += 1
    else:
        print("Opção inválida!")

# Resultados finais
print("\n===== RESULTADO DA PESQUISA =====")
print(f"Quantidade de respostas EXCELENTE: {excelente}")
print(f"Quantidade de respostas RUIM: {ruim}")
