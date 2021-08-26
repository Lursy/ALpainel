from menu import ip, num, cep, cnpj, placa, ascii
from menu.tools import *
from time import sleep
import os


# phonenumbers
try:
    import phonenumbers
except ModuleNotFoundError:
    print('Instalando...')
    os.system('python3 -m pip install --upgrade pip>&/dev/null/')
    os.system('pip install phonenumbers>&/dev/null/')
    import phonenumbers


# json
try:
    import json
except ModuleNotFoundError:
    print('Instalando...')
    os.system('python3 -m pip install --upgrade pip>&/dev/null/')
    os.system('pip install json>&/dev/null/')
    import json


# requests
try:
    import requests
except ModuleNotFoundError:
    os.system('python3 -m pip install --upgrade pip')
    os.system('pip install requests')
    import requests


try:
    clear()
    print(ascii.dra)
    sleep(2)
    clear()
    while True:
        print(ascii.alpainel)
        print(ascii.painel)
        esc = int(input(f'{am}//: '))
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
            root = os.system('su and exit>null')
            os.system('rm -rf null')
            if root == 0:
                print(f'{vd}Root ON')
            elif root == 256:
                print(f'{ve}Root OFF')
            else:
                print(f'{cy}Error')
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
except KeyboardInterrupt:
    print(f'{vd}Saindo...')
    sleep(2)
    clear()
