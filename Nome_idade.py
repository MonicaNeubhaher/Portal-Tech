# Code Park 31/10/22.py
# Monica Rodrigues Lopes Neubhaher
# Turma 03  - Professor Ravi Antunes
# Exercício - Desenvolver um programa que recebe do usuário nome completo e
#             ano de nascimento que seja entre 1922 e 2021.
#             A partir dessas informações, o sistema mostrará o nome do usuário
#             e a idade que completou, ou completará, no ano atual (2022).
#             Caso o usuário não digite um número ou apareça um inválido
#             no campo do ano, o sistema informará o erro e continuará
#             perguntando até que um valor correto seja preenchido.


while True:
    try:
        ano_atual = 2022
        nome_completo =  input("Informe o nome completo: ")
        ano_nasc = int(input("Informe o ano de nascimento entre 1922 e 2021: "))
        if ano_nasc >= 1922 and ano_nasc <= 2021:
            idade = ano_atual - ano_nasc
            print()
            print(f"{nome_completo} - {idade} anos")
            print()
            break
        else:
            print()
            print("Ano de nascimento informado fora da faixa")
            print()
    except:
        print()
        print("Ano incorreto! Tente novamente.")
        print()
