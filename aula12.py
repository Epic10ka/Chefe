from datetime import date, datetime


name = input('Digite seu nome: ').strip().title()
print()
if name == 'Lucas' or name == 'Epic':
    print('Bem vindo ao QG, Lucas!')
    ql= input('Deseja realizar alguma ação, chefe?: ').upper()
    if ql == 'SIM' or ql == 'S':
        print('\033[1;31mOPÇÕES'.center(30), '\n\033[1;36m(Calculadora)\033[m', '\n\033[1;35m(Jogo de adivinha)\033[m' )
        rl1 = input('\033[1mQual?: ').strip().upper()

       #CALCULADORA
        if rl1.startswith('CALC'):
            print('—='*15)
            print('\033[1;36mCÁLCULADORA\033[m'.center(35))
            print('—='*15)
            wich = input('Deseja fazer o cálculo de produtos, soma ou subtração?: ').strip().upper()
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
            elif wich.startswith('PRO'):
                p1 = float(input('Digite o primeiro valor: '))
                p2 = float(input('Digite o segundo valor: '))
                print(f'O produto é {p1*p2}')
                #CALCULADORA

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
elif 12 >= hora < 18:
    print(f'Tenha uma ótima tarde, {name}')
else:
    print(f'Tenha um a ótima noite, {name}')