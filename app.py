import os

restaurantes = [{'nome' : 'Praca', 'categoria': 'Japonesa', 'ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Pizza','ativo':True},
                {'nome' : 'Cantina', 'categoria': 'Italiano', 'ativo':False}]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitul('Finalizar app')
    
def voltar_ao_menu_principal():
      input('\nDigite uma tecla para voltar ao menu principal ')
      main()

def opcao_invalida():
    print('Opção inválida"\n')
    voltar_ao_menu_principal()

def exibir_subtitul(texto):
      os.system('cls')
      print(texto)
      print()

def cadastrar_novo_restaurante():
      exibir_subtitul('Cadastro de novos restaurantes\n')
      nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
      categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
      dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
      restaurantes.append(dados_do_restaurante)#empurrando variavel nome_do_restaurante para a lista restaurante
      print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
      voltar_ao_menu_principal()

def listar_restaurantes():
      exibir_subtitul('Listando restaurantes')

      for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria = restaurante['categoria']
            ativo = restaurante['ativo']
            print(f'.{nome_restaurante} | {categoria} | {ativo}')

      voltar_ao_menu_principal()

def alternar_estado_restaurante():
      exibir_subtitul('Alterando estado do restaurante')
      nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
      restaurante_encontrado = False
      for restaurante in restaurantes:
            if nome_restaurante == restaurante['nome']:
                restaurante_encontrado = True
                restaurante['ativo'] = not restaurante['ativo']
                mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso '
                print(mensagem)
      if not restaurante_encontrado:
            print('O restaurante não foi encontrado')

      voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
            # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1: 
                cadastrar_novo_restaurante()
                print('Cadastrar restaurante')
        elif opcao_escolhida == 2: 
                listar_restaurantes()
                print('Listar restaurantes')
        elif opcao_escolhida == 3: 
                alternar_estado_restaurante()
        elif opcao_escolhida == 4: 
                finalizar_app()
        else: 
                opcao_invalida()
    except:
          opcao_invalida

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
