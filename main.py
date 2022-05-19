import  time

while   True:
    print('Olá, você deseja multiplicar, dividir ou somar ?')
    print()
    print('1 opção - Multiplicar')
    print('2 opção - Dividir')
    print('3 opção - Somar')
    print('4 opção - Subtrair')
    print()
    print('5 opção - Fechar o Programa')
    print()
    optionvalue     =   int(input(':'))

# Primeira opção - Multiplicação
    if  optionvalue ==  1:
        print()
        print('Qual número você deseja multiplicar? digite.')
        multvalue   =   int(input(':'))
        print()
        print('{} vezes?'.format(multvalue))
        print()
        multvalue2  =   int(input(':'))
        if  multvalue   ==  325:
            if  multvalue2  ==  325:
                print()
                print('Você encontrou o Easter Egg (: ')

# parte lógica
        multresult  =   multvalue   *   multvalue2
    
        print()
        print('O resultado de {} vezes {} é {}'.format(multvalue,   multvalue2, multresult))
        time.sleep(10)
        print ("\n" * 130) 

# Segunda opção - Dividir
    if optionvalue  ==  2:
        print()
        print('Qual número você deseja dividir? digite.')
        divvalue    =   int(input(':'))
        print()
        print('{} divido em quantas vezes?'.format(divvalue))
        print()
        divvalue2   =   int(input(':'))

#parte lógica
        divresult   =   divvalue    /   divvalue2


        print()
        print('O resultado de {} divido por {} é {}'.format(divvalue,   divvalue2,  divresult))
        time.sleep(10)
        print ("\n" * 130) 

# Terceira opção - Somar
    if  optionvalue ==  3:
        print()
        print('Qual número você deseja somar? digite.')
        somvalue    =   int(input(':'))
        print()
        print('{} + ?'.format(somvalue))
        print()
        somvalue2   =   int(input(':'))

#parte lógica
        somresult   =   somvalue    +   somvalue2

        print ("\n" * 130)
        print('O resultado de {} + {} é {}'.format(somvalue,    somvalue2,  somresult))
        time.sleep(10)
        print ("\n" * 130) 

# Quarta opção - Subtração
    if  optionvalue ==  4:
        print()
        print('Qual número você deseja subtrair? digite.')
        subvalue    =   int(input(':'))
        print()
        print('{} - ?'.format(subvalue))
        print()
        subvalue2   =   int(input(':'))
#parte lógica
        subresult   =   subvalue    -   subvalue2

        print   ("\n"   *   130)
        print('O resultado de {} - {} é {}'.format(subvalue,    subvalue2,  subresult))
        time.sleep(10)
        print   ("\n"   *   130)

# Quinta opção  - Fechar Programa
    if  optionvalue ==  5:
        print('Fechando o Programa em 5 segundos...')
        print()
        time.sleep(1)
        print('5...')
        time.sleep(1)
        print('4...')
        time.sleep(1)
        print('3...')
        time.sleep(1)
        print('2...')
        time.sleep(1)
        print('1...')
        time.sleep(1)
        print('BYE')
        time.sleep(1)
        exit()
