from time import sleep
print('='*20)
v1 = int(input('Digite o 1º valor: '))
v2 = int(input('Digite o 2º valor: '))
print('='*20)
opção = 0
while opção != 5:
    print('''
    [ 1 ] Somar 
    [ 2 ] Multiplicar
    [ 3 ] Maior 
    [ 4 ] Novos números 
    [ 5 ] Sair do programa
    ''')
    opção = int(input('Qual opção você escolhe? '))
    if opção == 1:
        soma = v1 + v2
        print ('A soma entre {} + {} é {}.'.format(v1, v2, soma))
    elif opção == 2:
        produto = v1 * v2
        print('O resultado de {} x {} é {}.'.format(v1, v2, produto))
    elif opção == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print('Entre {} e {} o maior valor é {}.'.format(v1,v2, maior))
    elif opção == 4:
        print('NOVOS VALORES')
        v1 = int(input('Qual o 1º valor? '))
        v2 = int(input('Qual o 2º valor? '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')
