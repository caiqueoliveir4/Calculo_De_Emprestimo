casa =float(input('Valor da casa: R$'))
salário = float(input('Informe o seu salário: R$'))
anos = int(input('Deseja financiar sua casa em quantos anos?: '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para financiar a casa no valor de: R${:.2f} em {} anos'. format(casa, anos), end='')
print(' a prestação será de: R${:.2f}'.format(prestação))
if prestação <=mínimo:
    print('Emprestimo foi concedido.')
else:
    print('Emprestimo negado.')


