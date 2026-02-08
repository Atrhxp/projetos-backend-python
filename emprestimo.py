import os

print("SISTEMA DE EMPRÉSTIMO")

nome_cliente = input("Nome: ")
sobrenome = input("Sobrenome: ")
idade = int(input("Idade: "))
renda = float(input("Renda mensal: R$ "))
localizacao = input("Localização: ").lower()
valor_emprestimo = float(input("Valor do empréstimo: R$ "))
parcelas = int(input("Número de parcelas: "))


def aprovar_emprestimo(renda):
    if renda < 1500:
        print("\nEmpréstimo reprovado por renda insuficiente.")
        os._exit(0)
    else:
        print("\nEmpréstimo aprovado.")

aprovar_emprestimo(renda)



if renda < 2500:
    tipo_de_emprestimo = '1'
elif renda < 5000:
    tipo_de_emprestimo = '2'
else:
    tipo_de_emprestimo = '3'


def calculo_parcela_fixa(valor, tipo, meses):

    if tipo == '1':
        taxa = 0.05
        tipo_nome = "Empréstimo pessoal"
    elif tipo == '2':
        taxa = 0.03
        tipo_nome = "Empréstimo consignado"
    elif tipo == '3':
        taxa = 0.02
        tipo_nome = "Empréstimo com garantia"
    else:
        print("Tipo de empréstimo inválido.")
        return

    parcela = valor * (taxa * (1 + taxa) ** meses) / ((1 + taxa) ** meses - 1)
    total_pago = parcela * meses
    juros = total_pago - valor

    print("\nRESULTADO FINAL")
    print(f"Cliente: {nome_cliente} {sobrenome}")
    print(f"Tipo: {tipo_nome}")
    print(f"Parcelas: {meses}")
    print(f"Parcela fixa: R$ {parcela:.2f}")
    print(f"Total pago: R$ {total_pago:.2f}")
    print(f"Juros totais: R$ {juros:.2f}")


calculo_parcela_fixa(valor_emprestimo, tipo_de_emprestimo, parcelas)
