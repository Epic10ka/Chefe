from datetime import date, datetime
#about var
#q = question
#rl = resposta lucas

name = input('Digite seu nome: ').strip().title()
print()
if name == 'Lucas' or name == 'Epic':
    print('Bem vindo ao QG, Lucas!')
    ql= input('Deseja realizar alguma ação, chefe?: ').upper()
    if ql == 'SIM' or ql == 'S':
        print('\033[1;31mOPÇÕES'.center(30), '\n\033[1;36m(Calculadora)\033[m', '\n\033[1;35m(Guessing Game)\033[m' )
        rl1 = input('\033[1mQual?: ').strip().upper()

       #CALCULADORA
        if rl1.startswith('CAL'):
            print('—='*15)
            print('\033[1;36mCÁLCULADORA\033[m'.center(35))
            print('—='*15)
            wich = input('Deseja fazer o cálculo de \033[1;35m produtos \033[m, \033[1;34m soma \033[m ou \033[1;31m subtração\033[m?: ').strip().upper()
            if wich.startswith('SOMA'):
                print()
                print('—='*6)
                print('\033[1;34m SOMA \033[m'.center(22))
                print('—='*6)
                n1 = float(input('Digite o primeiro valor: '))
                n2 = float(input('Digite o segundo valor: '))
                print(f'A soma é: {n1+n2}')
            elif wich.startswith('SUB'):
                print('—='*6)
                print('\033[1;31m SUBTRAÇÃO \033[m'.center(22))
                print('—='*6)
                s1 = float(input('Digite o primeiro valor: '))
                s2 = float(input('Digite o segundo valor: '))
                print(f'A subtração é : {s1-s2}')
            elif wich.startswith('PRO') or wich.startswith('MUL'):
                print('—='*10)
                print('\033[1;35mMULTIPLICAÇÃO\033[m'.center(30))
                print('—='*10)
                p1 = float(input('Digite o primeiro valor: '))
                p2 = float(input('Digite o segundo valor: '))
                print(f'O produto é {p1*p2}')
                #CALCULADORA

                #GUESSING GAME
        if rl1.startswith('JOGO') or rl1.startswith('GUESS') or rl1.startswith('GAME'):
            print('—='*15)
            print('\033[1;35mADIVINHAÇÃO / GUESSING GAME\033[m'.center(40))
            print('—='*15)
            from random import randint
            num = randint(0,5)
            guess_q = int(input('Digite um numero de 0 a 5: '))
            if guess_q == num:
                print(f'\033[1;32mPARABÉNS\033[m, você acertou! O número era \033[4;36m{num}\033[m')
            else:
                print(f'Ah, que pena, \033[1:31mVOCÊ ERROU\033[m. O número era \033[4;36m{num}\033[m')
                #GUESSING GAME
    else:
        print('Ok')
elif name.startswith('Cris'):
    print('Bem vinda ao QG, Cris!')
else:
    print(f'Olá, {name}')

hora = datetime.now().hour
print()
if 6 <= hora < 12:
    print(f'Tenha uma ótima manhã, {name}')
elif 12 <= hora < 18:
    print(f'Tenha uma ótima tarde, {name}')
else:
    print(f'Tenha uma ótima noite, {name}')