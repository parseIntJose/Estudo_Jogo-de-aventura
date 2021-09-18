import random
import math
from time import sleep

nome = input("Digite seu nome: ")
dados = [1,2,3,4,5,6]
resultado = random.choice(dados)
print(f"\n ola {nome}")
print("A sua aventura depende do numero que o dado cair")
print(f"O numero do dado é {resultado}")

if resultado == 1:
    print("\n Essa é a aventura numero 1")
    print(f"Você {nome} estava procurando um emprego \n")
    print("""Você tem 3 opções para entregar curriculos:
    [1] Mercado
    [2] Padaria
    [3] Firma\n""")
    contratacao = int(input("Qual deseja escolher? "))

    if contratacao == 1:
        print("Você foi recusado.")
        print("GAME OVER")
    
    elif contratacao == 2:
        print("Você passou agora recebe um salario de 1.100 R$")
        print("O que deseja fazer agora?\n")
        print("""Suas opções são:
        [1] Juntar para uma moto
        [2] Fazer um curso de progamação
        [3] Curtir na Balada\n""")
        contratacao = int(input("Qual deseja fazer? "))

        if contratacao == 1:
            print("Você comprou a moto mas roubaram depois de 3 dias")
            print("Game over")

        elif contratacao == 2:
            print("Você virou um progamador Full stack e esta ganhando muito dinheiro")
            print("Você conquistou tudo que queria")
            print("-=" * 12)
            print("VOCÊ GANHOU!!")
            print("-=" * 12)

        else:
            print("Você foi morto em uma briga de bar")
            print("GAME OVER")

    else:
        print("Você passou na firma e agora so anda de uno com escada")
        print("-=" * 12)
        print("VOCÊ GANHOU NA VIDA")
        print("-=" * 12)

elif resultado == 2:
    print("\n Essa é a aventura numero 2")
    print(f"Você {nome} está em um cassino. E você tem uma divida para pagar\n")
    print("Sendo assim tem que apostar para tentar ganhar\n")
    print("Você tem 3 opções de aposta")
    print("""Suas opções são:
    [1] Black Jack
    [2] Roleta de premios
    [3] Poker\n""")
    aposta = int(input("Qual vai escolher? "))

    if aposta == 1:
        print("Você foi pego trapaceando e foi morto")
        print("GAME OVER")
    
    elif aposta == 2:
        premios = ["Casa", "Carro", "4.500$", "Perde tudo", "75.000 Fichas"]
        premio = random.choice(premios)
        print(f"Bem vindo a roleta {nome}")
        print(f"Aqui estão os premios que você pode ganhar: {premios}\n")
        print("Tudo depende da sua sorte\n")
        print("Girando em")
        print("3")
        sleep (1)
        print("2")
        sleep (1)
        print("1")
        sleep (1)
        print("GIRANDO...")

        if premio == "Casa":
            print(f"Você Ganhou: {premio}\n")
            print("-=" * 12)
            print("VOCÊ GANHOU O MELHOR PREMIO DE TODOS PARABENS!!!")
            print("-=" * 12)
            print("")
            print("VOCÊ VENCEU!!")
        
        elif premio == "Carro":
            print(f"Você Ganhou: {premio}\n")
            print("Você teve que entregar para pagar a divida")
            print("GAME OVER")
        
        elif premio == "4.500$":
            print(f"Você Ganhou: {premio}\n")
            print("Não foi o suficiente para paagr a divida")
            print("Game over")
        
        elif premio == "Perde tudo":

            print("Você perdeu tudo e foi morto por causa da divida")
            print("GAME OVER")

        elif premio == "75.000 Fichas":
            print(f"Você Ganhou: {premio}\n")
            print("Você conseguiu pagar a divida e ainda sobrou dinheiro\n")

            print("-=" * 12)
            print("Você venceu!!!")
            print("-=" * 12)
        
    else:
        print("Você perdeu tudo que tinha")
        print("GAME OVER")

elif resultado == 3:
    print("\n Essa é a aventura numero 3")
    print(f"Você {nome} está em alto mar pescando ate que algo bate no barco")
    print("Você percebe que danificou o casco do barco")
    print("Você tem algumas opções para tentar resolver")
    print("""Suas opções são:
    [1] Continuar navegando
    [2] Chamar a guarda costeira
    [3] Tentar reparar o barco\n""")
    opcoes = int(input("Qual deseja fazer? "))

    if opcoes == 1:
        print("Você afundou o barco e morreu")
        print("GAME OVER")
    
    elif opcoes == 2:
        print("O Tempo ficou nevoado você precisa sinalizar sua localização\n")
        print("Suas opções são:")
        print("""
        [1] Sinalizador antigo
        [2] Fazer fogo
        [3] Gritar\n""")
        opcoes = int(input("Qual deseja fazer? "))

        if opcoes == 1:
            print("Ele não funcionou totalmente mas foi o suficiente\n")
            print("-=" * 12)
            print("VOCÊ GANHOU!!!")
            print("-=" * 12)
        
        elif opcoes == 2:
            print("Você colocou fogo no barco e morreu")
            print("GAME OVER")
        
        else:
            print("Não gritou alto o suficiente e o barco afundou\n")
            print("GAME OVER")

    else:
        print("Não funcionou e o barco afundou")
        print("GAME OVER")

elif resultado == 4:
    print("\n Essa é a aventura numero 4")
    print(f"Você {nome} estava fazendo uma trilha com seus amigos")
    print("ate que você se perdeu deles\n")
    print("Você tem algumas opções para achar eles")
    print("""Suas opções são:
    [1] Continuar andando
    [2] Procurar um lugar seguro
    [3] Fazer uma fogueira\n""")
    trilha = int(input("Qual deseja fazer? "))

    if trilha == 1:
        print("Você não achou nada e morreu de sede")
        print("GAME OVER")
    
    elif trilha == 2:
        print("Você achou um lugar seguro e todos seus amigos estavam la\n")
        print("-=" * 12)
        print("VOCÊ VENCEU!!")
        print("-=" * 12)
    
    else:
        print("Você fez a fogueira errado e colocou fogo na floresta")
        print("Você foi preso")
        print("GAME OVER")
    
elif resultado == 5:
    print("\n Essa é a aventura numero 5")
    print(f"Você {nome} estava participando de um roubo")
    print("A policia entrou no local e pediu para vocês se renderem")
    print("O que deseja fazer?\n")
    print("""
    [1] Render-se
    [2] Atirar
    [3] Fugir\n""")
    escolhas = int(input("Qual deseja fazer? "))

    if escolhas == 1:
        print("Você foi preso por 10 anos")
        print("GAME OVER")
    
    elif escolhas == 2:
        print("Você e todos seus amigos morreram na troca de tiros")
        print("GAME OVER")

    else:
        print("Vocês entraram no carro e em seguida foram baleados")
        print("GAME OVER")

else:
    print("\n Essa é a aventura numero 6\n")
    print(f"Você {nome} está em uma caverna")
    print("e sente um tremor, percebe que a saida se fechou\n")
    print("Você tem 3 opçôes para sair\n")
    print("""
    [1] Cavar a entrada
    [2] Esperar por ajuda
    [3] Jogar dinamite na entrada\n""")
    mineracao = int(input("Qual deseja fazer? "))

    if mineracao == 1:
        print("Você conseguiu cavar e chamar ajuda")

        print("-=" * 12)
        print("VOCÊ VENCEU!!")
        print("-=" * 12)
    
    elif mineracao == 2:
        print("Ninguem foi te ajudar e você morreu")
        print("GAME OVER")
    
    else:
        print("VocÊ explodiu tudo e a caverna desabou em cima de você")
        print("GAME OVER")