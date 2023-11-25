import advinhacao
import forca

def escolhe_jogo():
    print("**********************************")
    print("Bem-vindo a um jogo de adivinhacao")
    print("**********************************")

    print("(1) Forca (2) Adivinhação")

    jogo =int(input("Qual o jogo?"))

    if(jogo ==1):
        forca.jogar()
    else:
        adivicao.jogar()

if __name__ == "__main__":
    escolhe_jogo()

