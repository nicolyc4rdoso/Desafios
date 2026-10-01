# Crie uma função chamada cumprimentar ela deve receber o nome e a hora, essa função deve gerar cumprimentos baseado no periodo do dia
# Periodos :    Manhã: 5 até 12, Tarde: 13 até 18, Noite: 18 até 24

# Exemplo: 
# Nome: Allana
# Hora : 9
# Bom dia, Allana

# Exemplo2: 
# Nome: Gustavo B
# Hora : 15
# Boa Tarde, Gustavo B

def cumprimentar(nome, hora):
    if hora >= 5 and hora <= 12:
        print(f"Bom dia, {nome}")
    elif hora >= 13 and hora <= 18:
        print(f"Boa tarde, {nome}")
    elif hora >= 19 and hora <= 24:
        print(f"Boa noite, {nome}")
    else:
        print("Horário inválido")


nome = input("Nome: ")
hora = int(input("Hora: "))

cumprimentar(nome, hora)