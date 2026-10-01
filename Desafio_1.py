# Faça um código que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
# Exemplo de Resultado: O Seu salário atual é de R$1500,00 com o aumento de 15% seu novo salário será de R$1725,

salario = float(input("Digite seu salário :"))
aumento = salario * 0.15
salario_com_aumento = salario + aumento
print(f"O seu salário atual é {salario}, com aumento de {aumento}, seu novo salário {salario_com_aumento:.2f}")
