nome = input('Digite seu nome: ')
data_ingresso = input(nome + ', digite o ano de ingresso na universidade: ')
confirma = input('Confirma que o ano de ingresso foi ' + data_ingresso + '? Digite s para sim e n para não: ')

while confirma != 's':
    data_ingresso = input('Digite outro ano de ingresso: ')
    confirma = input('Confirma que o ano de ingresso foi ' + data_ingresso + '? Digite s para sim e n para não: ')

print('Obrigada pelas informações, ' + nome + '!')