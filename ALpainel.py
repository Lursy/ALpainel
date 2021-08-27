import os
try:
    import phonenumbers
except ModuleNotFoundError:
    print('Instalando...')
    os.system('python3 -m pip install --upgrade pip')
    os.system('pip install phonenumbers')
    import phonenumbers
try:
    import json
except ModuleNotFoundError:
    print('Instalando...')
    os.system('python3 -m pip install --upgrade pip')
    os.system('pip install json')
    import json
try:
    import requests
except ModuleNotFoundError:
    os.system('python3 -m pip install --upgrade pip')
    os.system('pip install requests')
    import requests
from menu import cnpj, num, placa, ip, cep, ascii
from menu.tools import *
from time import sleep


try:
    clear()
    print(ascii.dra)
    sleep(2)
    clear()
    while True:
        try:
            print(ascii.alpainel)
            print(ascii.painel)
            esc = int(input(f'{am}//: '))
            try:
                if esc == 1:
                    clear()
                    cnpj.ccnpj()
                elif esc == 2:
                    clear()
                    cep.ccep()
                elif esc == 3:
                    clear()
                    ip.cip()
                elif esc == 4:
                    clear()
                    placa.cplaca()
                elif esc == 5:
                    clear()
                    num.numeros()
                elif esc == 6:
                    root()
                    sleep(3)
                    clear()
                elif esc == 7:
                    clear()
                    ip.mip()
                elif esc == 8:
                    os.system(f'termux-open-url https://www.youtube.com/channel/UCwmkiKIZHL1wscYHfIINZKw')
                    clear()
                elif esc == 9:
                    print(f'{vd}Saindo...')
                    sleep(1)
                    clear()
                    break
                else:
                    print(f'{ve}Comando inválido!')
                    sleep(1)
                    clear()
            except ValueError:
                print(f'{ve}Erro de digitação'
                      f'{am}[1] {cy}menu'
                      f'{am}[2] {cy}Sair')
                error = str(input(f'{am}//:'))
                if error[0] == '1':
                    pass
                if error[0] == 2:
                    print(f'{vd}Saindo...')
                    sleep(2)
                    clear()
                    exit()
                else:
                    print(f'{ve}Error')
                    sleep(10)
        except ValueError:
            print(f'{ve}Erro de digitação')
            sleep(2)
            clear()
        except requests.exceptions.ConnectionError:
            print(f'{ve}Internet necessaria para executar esta função')
            sleep(2)
            clear()
except KeyboardInterrupt:
    print(f'\n{vd}Saindo...')
    sleep(2)
    clear()
