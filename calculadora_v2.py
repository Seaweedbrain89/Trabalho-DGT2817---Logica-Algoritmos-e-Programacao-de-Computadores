# Variável para controle da saída
saida = ''

# Função de adição
def adicao(a, b):
    return a + b

# Exemplo de uso da função
resultado = adicao(8, 5)
print("Resultado da adição:", resultado)

# Função de subtração
def subracao(a, b):
    return a - b

# Exemplo de uso da função
resultado = subracao(7, 3)
print("Resultado da subtração:", resultado)

# Função de multiplicação
def multiplicacao(a, b):
    return a * b

# Exemplo de uso da função
resultado = multiplicacao(9, 10)
print("Resultado da multiplicação:", resultado)

# Função de divisão
def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return a / b

# Exemplo de uso da função
resultado = divisao(55, 2)
print("Resultado da divisão:", resultado)

resultado_zero = divisao(98, 0)
print(resultado_zero)

# Funções de operações
def adicao(a, b):
    return a + b

def subracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return a / b

# Função calculadora
def calculadora(num1, num2, operacao):
    if operacao == '+' or operacao.lower() == 'adicao':
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao.lower() == 'subtracao':
        resultado = subracao(num1, num2)
    elif operacao == '*' or operacao.lower() == 'multiplicacao':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/' or operacao.lower() == 'divisao':
        resultado = divisao(num1, num2)
    else:
        return "Operação inválida"
    
    return resultado

# Exemplo de uso da função calculadora
num1 = 10
num2 = 5

resultado = calculadora(num1, num2, '+')
print("Resultado da adição:", resultado)

resultado = calculadora(num1, num2, '-')
print("Resultado da subtração:", resultado)

resultado = calculadora(num1, num2, '*')
print("Resultado da multiplicação:", resultado)

resultado = calculadora(num1, num2, '/')
print("Resultado da divisão:", resultado)

resultado = calculadora(num1, num2, 'modulo')  # Exemplo de operação inválida
print(resultado)

# Funções de operações
def adicao(a, b):
    return a + b

def subracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return a / b

# Função calculadora
def calculadora(num1, num2, operacao):
    if operacao == '+' or operacao.lower() == 'adicao':
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao.lower() == 'subtracao':
        resultado = subracao(num1, num2)
    elif operacao == '*' or operacao.lower() == 'multiplicacao':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/' or operacao.lower() == 'divisao':
        resultado = divisao(num1, num2)
    else:
        return "Operação inválida"
    
    return resultado

# Variável para controle da saída
saida = ''

# Laço while para executar a calculadora
while saida.lower() != 'n':
    # Entrada do usuário
    primeiro_numero = float(input("Digite o primeiro número: "))
    segundo_numero = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, / ou seu nome): ")

    # Chamando a função calculadora
    resultado = calculadora(primeiro_numero, segundo_numero, operacao)

    # Exibindo o resultado
    print('Resultado da operação: ' + str(resultado))

    # Perguntando se deseja continuar
    saida = input("Deseja continuar? (Digite 's' para sim ou 'n' para não): ")

print("Programa encerrado.")
