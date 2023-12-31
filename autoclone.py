#!/C:/Users/ALUNO/AppData/Local/Microsoft/WindowsApps/python3.exe

import subprocess
import os
from colorama import Fore


def clone_repo(user_name, repo_name, destination_path):
    os.chdir(destination_path)

    clone_command = f'git clone https://github.com/{user_name}/{repo_name}'
    cloning = subprocess.run(clone_command, shell=True)

    if (cloning.returncode != 0):
        print('')
        print(
            f'{Fore.RED}Não foi possível fazer a clonagem do repositório "{repo_name}"')
        print('')
        print(f'{Fore.WHITE}Verifique: ')
        print(
            f'{Fore.YELLOW}Verifique se o nome do usuário "{user_name}" está correto.')
        print(
            f'{Fore.YELLOW}Verifique se o nome do repositório "{repo_name}" está correto.')
        print(
            f'{Fore.YELLOW}Se não nenhum arquivo ou pasta com o nome de "{repo_name}" existe no local de destino.')

    else:
        print('')
        print(f'{Fore.GREEN}O repositório "{repo_name}" foi clonado com sucesso!')

        open_command = f'code {destination_path}/{repo_name}'
        subprocess.run(open_command, shell=True)

        print(f'{Fore.YELLOW}Abrindo no Visual Code...')


while True:
    print(f'{Fore.WHITE}')
    print('--------------------------')
    print('--------AUTOCLONE---------')
    print('--------------------------')
    print('Menu: ')
    print('')
    print('1. Clonar repositório público')
    print('0. Encerrar')
    print('')

    option = int(input('Escolha uma opção: '))

    if (option == 0):
        print(f'{Fore.YELLOW}Encerrando AutoClone...')
        break

    elif (option == 1):
        print('--------------------------')
        user_name = input(
            'Digite o nome do usuário proprietário do repositório: ')
        repo_name = input('Digite o nome do repositório público: ')

        try:
            if (len(user_name) != 0 and len(repo_name) != 0):
                clone_repo(user_name, repo_name, 'C:/Users/ALUNO/Desktop/')

            else:
                raise Exception(
                    'Verifique se os nomes do usuário e/ou repositório estão corretos.')

        except Exception as e:
            print(f'{Fore.RED}{e}')
    else:
        print(f'{Fore.YELLOW}Digite uma opção válida.')
