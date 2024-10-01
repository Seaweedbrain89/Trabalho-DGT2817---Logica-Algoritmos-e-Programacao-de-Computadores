# Atribuindo um valor inicial à variável entrada_idade
entrada_idade = ''

# Instrução while que continua enquanto entrada_idade for diferente de '0'
while entrada_idade != '0':
    entrada_idade = input('Digite um número qualquer ou 0 para sair: ')
    
    # Imprimindo o número digitado, caso não seja '0'
    if entrada_idade != '0':
        print(f'Número digitado: {entrada_idade}')
