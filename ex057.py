sexo = str(input('Digite o seu sexo [M/F]:')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = input('Opção inválida digite seu sexo [M / F]:').strip().upper()[0]
print('Sexo {} foi registrado com sucesso.'.format(sexo))

