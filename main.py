from random import randint

def jogadadobot() :
    return randint(1,3)

def bemvindo() :
    print('-'*20)
    print('Bem Vindo Ao Jokempô')
    print('-'*20)

def msg():
    print('  Escolha a Jogada')
    print('1. Pedra')
    print('2. Papel')
    print('3. Tesoura')

def escolhaPedra(a,b):
    if escolha == 1 and escolhabot == 1 :
        print('-' * 10)
        print('O bot Botou Pedra Logo você :')
        print('EMPATOUUUUUUU')
        print('-' * 10)
    elif escolha == 1 and escolhabot == 3 :
        print('-' * 10)
        print('O bot Botou Tesoura Logo você :')
        print('Ganhouuuu , Parabens carai')
        print('-' * 10)
    elif escolha == 1 and escolhabot == 2:
        print('-' * 10)
        print('O bot Botou Papel Logo você :')
        print('Se fudeu')
        print('-' * 10)

def escolhaPapel(a,b):
    if escolha == 2 and escolhabot == 1 :
        print('-' * 10)
        print('O bot Botou Pedra Logo você :')
        print('Ganhouuuu , Parabens carai')
        print('-' * 10)
    elif escolha == 2 and escolhabot == 3 :
        print('-' * 10)
        print('O bot Botou Tesoura Logo você :')
        print('Se fudeu')
        print('-' * 10)
    elif escolha == 2 and escolhabot == 2:
        print('-' * 10)
        print('O bot Botou Papel Logo você :')
        print('EMPATOUUUUUUU')
        print('-' * 10)

def escolhaTesoura(a,b):
    if escolha == 3 and escolhabot == 1 :
        print('-' * 10)
        print('O bot Botou Pedra Logo você :')
        print('Se fudeu')
        print('-' * 10)
    elif escolha == 3 and escolhabot == 3 :
        print('-' * 10)
        print('O bot Botou Tesoura Logo você :')
        print('EMPATOUUUUUUU')
        print('-' * 10)
    elif escolha == 3 and escolhabot == 2:
        print('-' * 10)
        print('O bot Botou Papel Logo você :')
        print('Ganhouuuu , Parabens carai')
        print('-' * 10)



cnt = 's'

while cnt == 's' :
    bemvindo()
    msg()
    escolha = int(input('Minha Escolha é : '))
    escolhabot = jogadadobot()
    if escolha == 1:
        escolhaPedra(escolha, escolhabot)
    elif escolha == 2:
        escolhaPapel(escolha, escolhabot)
    else :
        escolhaTesoura(escolha, escolhabot)

    cnt = input('Deseja uma Nova Partida ? (S/N)').lower()
    if cnt == 'n':
        print('Programa Finalizado!!')
    else:
        print('--Reiniciando--')




