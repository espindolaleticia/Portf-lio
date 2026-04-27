#CADASTRO DOAÇÃO DE SANGUE
#nome
#peso
#altura
#idade
#tem peso minimo para doar
#tem idade minima para doar
print('Cadastro de doadores de sangue')
nome = input ('Por favor, digite seu nome: ')
peso = float(input('Por favor, digite seu peso: '))
altura = float(input('Por favor, digite sua altura: '))
ano_de_nascimento = int(input('Por favor, digite seu ano de nascimento: '))

idade = 2026 - ano_de_nascimento
tem_peso_minimo = peso > 50
tem_idade_minima = idade >= 16

texto_saída = f'\tNOME: {nome}\n\tPESO: {peso}\n\tALTURA: {altura}cm\n\tIDADE: {idade}\n\tTEM PESO MINÍMO PARA DOAR?: {tem_peso_minimo}\n\tTEM IDADE PARA DOAR?: {tem_idade_minima}'
print(texto_saída)