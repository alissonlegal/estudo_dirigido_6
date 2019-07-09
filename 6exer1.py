'''
 1) F.U.P. para controlar os produtos que um pequeno comércio vende. Você deve
solicitar ao usuário o código do produto e quantos itens irá comprar. Utilize a
seguinte sequência de códigos para registrar suas vendas:
 Código | Preço |
 10 | 5,00 |
 20 | 10,00 |
 33 | 50,00 |
 45 | 77,00 |
 88 | 55,00 |
'''

apagar = 0

while True:
    codigo = int(input("Codigo do produto (0 para SAIR): "))
    preco = 0
    if codigo == 0:
        break
    elif codigo == 10:
        preco = 5.00
    elif codigo == 20:
        preco = 10.00
    elif codigo == 33:
        preco = 50.00
    elif codigo == 45:
        preco = 77.00
    elif codigo == 88:
        preco = 55.00
    else:
        print("codigo invalido!")
    if preco != 0:
        quantidade = int(input("Quantidade: "))
        apagar = apagar + (preco * quantidade)
    print("Total a pagar R$ %.2f" %apagar)
