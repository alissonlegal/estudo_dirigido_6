'''
4) F.U.P. para verificar se você é elegível a obter um empréstimo bancário para
aquisição de um imóvel. O programa deve perguntar ao usuário o valor do imóvel, o
salário do adquirente e a quantidade de anos a pagar. O valor da prestação mensal
não dever ultrapassar 30% do salário do comprador. Calcule o valor da prestação como
sendo o valor da casa a ser adquirida dividido pela quantidade de meses a pagar.
'''

valor = float(input("Digite o valor da casa: "))
salario = float(input("Digite o salario: "))
anos = int(input("Quantos anos: "))
meses = anos*12
prestacao = valor / meses
if prestacao > salario * 0.3:
    print("Infelizmente não da...")
else:
    print("Valor da prestacaoÇ R$%.2f. Emprestimo ok" % prestacao)
