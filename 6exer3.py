'''
3) F.U.P. para calcular o que você tem a pagar de energia elétrica à agência
fornecedora. O usuário deve inserir a quantidade de kWh consumidos e o tipo de
instalação: Residencial, Industrial ou Comércio. Calcule o preço a pagar pela tabela
abaixo:
 Código | Faixa(kWh) | Preço |
 Residência | Até 500 | 0,40 |
 | Acima de 500 | 0,65 |
 Comercial | Até 1000 | 0,55 |
 | Acima de 1000 | 0,60 |
 Indústria | Até 5000 | 0,55 |
 | Acima de 5000 | 0,60 |
'''
consumo = int(input("Consumo em kwh: "))
tipo = input("Tipo de estabelecimento (R, C ou I): ")
if tipo == "R":
    if consumo <= 500:
        preco = 0.40
    else:
        preco = 0.65
elif tipo == "C":
    if consumo <= 1000:
        preco = 0.55
    else:
        preco = 0.60
elif tipo == "I":
    if consumo <= 5000:
        preco = 0.55
    else:
        preco = 0.60
else:
    preco=0
    print("Erro! Tipo de estabelecimento desconhecido!")
consumoPagar = consumo * preco
print("Valor a pagar: R$%.2f " % consumoPagar)