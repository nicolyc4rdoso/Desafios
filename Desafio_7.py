# Crie uma função que calcule o valor da gorjeta de um garçom, baseada na qualidade do serviço
# qualidade_servico: 'ruim', 'medio', 'bom', 'excelente'

# A função deve pedir o valor da conta e a qualidade do serviço
# Se a qualidade for ruim a gorjeta é 0
# Se a qualidade for media a gorjeta é %2.5 do valor da conta
#Se a qualidade for bom a gorjeta é %4 do valor da conta
#Se a qualidade for excelente a gorjeta é %5 do valor da conta

#Exemplo:
# valor_conta = 100
# qualidade_servico = 'excelente'
# o valor da gorjeta é de R$ 5,00

def calcular_gorjeta(valor_conta, qualidade_servico):
    if qualidade_servico == "ruim":
        gorjeta = 0
    elif qualidade_servico == "medio":
        gorjeta = valor_conta * 0.025
    elif qualidade_servico == "bom":
        gorjeta = valor_conta * 0.04
    elif qualidade_servico == "excelente":
        gorjeta = valor_conta * 0.05
    else:
        print("Qualidade de serviço inválida")
        return

    print(f"O valor da gorjeta é de R$ {gorjeta:.2f}")


valor_conta = float(input("Digite o valor da conta: R$ "))
qualidade_servico = input("Digite a qualidade do serviço: ")

calcular_gorjeta(valor_conta, qualidade_servico)