'''
5) F.U.P. para controlar a utilização de lugares em uma sala de cinema. Imagine que
a lista Salas = [10,2,1,3,0] contenha o número de lugares vagos nas salas 1, 2, 3, 4
e 5, respectivamente. Seu programa lerá o número da sala e a quantidade de lugares
solicitados. Ele deve também informar se é possível vender o número de lugares
solicitados, ou seja, se ainda há lugares livres. Caso seja possível vender os
bilhetes, utilizará o número de lugares livres. A saída do programa deve ocorrer
quando o usuário digitar o número 0 (zero).
'''

lugares_vagos = [10, 2, 1, 3, 0]
while True:
    sala = int(input("Digite o numero da sala (SAIR = 0): "))
    if sala == 0:
        print("Saindo...")
        break
    if sala > len(lugares_vagos) or sala < 1:
        print("Sala invalida!")
    elif lugares_vagos[sala - 1] == 0:
        print("Não há lugares. Sala lotada!")
    else:
        lugares = int(input(f"Quantos lugares deseja? Tenho {(lugares_vagos[sala -1])} lugares vagos "))
        if lugares > lugares_vagos[sala -1]:
            print("Quantidade indisponivel! ")
        elif lugares < 0:
            print("Numero invalido")
        else:
            lugares_vagos[sala-1] -= lugares
            print(f"{lugares} lugares vendidos")
print("Utilizacao das salas!")
