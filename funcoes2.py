# Definindo a função loginUsuario
def loginUsuario(perfil):
    # Verificando se o valor do parâmetro perfil é igual a 'admin' (ignorando maiúsculas/minúsculas)
    if perfil.lower() == 'admin':
        print('Bem-vindo, Administrador')
    else:
        print('Bem-vindo, Usuário')

# Exemplo de chamada da função
loginUsuario(input("Digite seu perfil (admin ou usuário): "))

# Chamadas da função com diferentes valores
loginUsuario('Admin')
loginUsuario('admin')
loginUsuario('User')
loginUsuario('usuário')
loginUsuario('administrator')
loginUsuario('ADMIN')