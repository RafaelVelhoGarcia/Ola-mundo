from time import sleep
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
text = False
while text == False:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] SAIR DO PROGRAMA''')
    opcao = int(input('>>>>>>Qual a sua opçao:'))
    if opcao == 1:
        print('A soma entre {} + {} é {}'.format(n1,n2,(n1+n2)))
    elif opcao == 2:
        print('O produto entre {} X {} é {}'.format(n1,n2,(n1*n2)))
    if opcao == 3:
        if n1 > n2:
            maior = n1
        elif n1 == n2:
            maior = 'nenhum,porque eles tem o mesmo valor'
        else:
            maior = n2
        print('O comparando os números {} e {} o maior é {}'.format(n1,n2,maior))
    if opcao == 4:
        n1 = int(input('Digite um primeiro número:'))
        n2 = int(input('Digite um segundo número:'))
    print('=-=' * 10)
    if opcao == 5:
        print('Finalizando...')
        sleep(2)
        print('Fim do programa! Volte sempre!')
        text = True
    else:
        print('Opção invalida tente novamente')
