import random

def jogar():
    print("**********************************")
    print("Bem-vindo a um jogo de adivinhacao")
    print("**********************************")

    pontos = 1000
    rodada = 1
    total_de_tentativas = 0
    # XXXEssa função seria sem usar o random range contudo, isso faz com que nosso codigo tenha o problema do zero poder ser definido

    #numero_secreto = round(random.random() * 100)

    numero_secreto = random.randrange(1,101)

    print("Qual o nivel de dificuldade?")

    print("(1) Fácil (2) Médio (3) dificil")

    nivel = int(input("Define o nível:"))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas: 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite o seu número: ")
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Voce deve digitar um numero de 1 a 100! ", chute_str)
            continue


        acertou         = chute == numero_secreto
        chute_foi_maior = chute > numero_secreto
        chute_foi_menor = chute < numero_secreto

        if(acertou):
            print("voce acertou e fez {} pontos".format(pontos))
            break
        else:
            if(chute_foi_maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif(chute_foi_menor):

                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim de Jogo")

if __name__ == ("__main__"):
    jogar()
