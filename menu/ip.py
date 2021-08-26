from menu.ascii import *
from menu.tools import *
import requests
import json


def cip():
    print(alpainel)
    ip = str(input(f'{am}IP: {vd}'))
    if '.' in ip and ip.replace('.', '').isnumeric():
        d = requests.get(f'http://ip-api.com/json/{ip}')
        ret = json.loads(d.text)
        if f'""status":"fail"' in d:
            print(f'{ve}O ip digitado não existe ou foi escrito incorretamente!')
            sleep(2)
            clear()
            cip()
        clear()
        print(alpainel)
        print(f'{vd}IP: {am}{ip}\033[m\n'
              f'{vd}Pais:{am} {ret["countryCode"]} {br}➤{am} {ret["country"]}\n'
              f'{vd}Cidade: {am}{ret["city"]}\n'
              f'{vd}Latitude:{am} {ret["lat"]}\n'
              f'{vd}Longitude:{am} {ret["lon"]}\n')
        print(f'{ve}━' * 43)
        print(f'{am}[1] {cy}Menu\n'
              f'{am}[2] {cy}Consultar novamente\n'
              f'{am}[3] {cy}Sair')
        voltar = str(input(f'{am}//: {vd}'))
        if '1' in voltar[0]:
            clear()
        elif '2' in voltar[0]:
            clear()
            cip()
        elif '3' in voltar[0]:
            clear()
            print(f'{vd}Saindo...')
            exit()
        else:
            print(f'{ve}Comando não identificado')
            sleep(2)
            clear()
    else:
        print(f'{ve}Error {ip} não possui pontuação'
              if not '.' in ip else f'{am}Digite corretamente {ve}({ip})')
        sleep(1)
        clear()
        cip()


def mip():
    print(alpainel)
    req = requests.get('https://www.meuip.com.br/').text
    a = req.find('Meu ip é')
    b = req.find('</h3>')
    c = req[a + 9:b]
    d = requests.get(f'http://ip-api.com/json/{c}').text
    ret = json.loads(d)
    print(f'{vd}IP atual:{am} {c}\n'
          f'{vd}Pais:{am} {ret["countryCode"]} {br}➤{am} {ret["country"]}\n'
          f'{vd}Cidade: {am}{ret["city"]}\n'
          f'{vd}Latitude:{am} {ret["lat"]}\n'
          f'{vd}Longitude:{am} {ret["lon"]}\n')
    print(f'{ve}━' * 43)
    print(f'{am}[1] {cy}Menu\n'
          f'{am}[2] {cy}Ver novamente\n'
          f'{am}[3] {cy}Sair')
    voltar = str(input(f'{am}//: {vd}'))
    if '1' in voltar[0]:
        clear()
    elif '2' in voltar[0]:
        clear()
        mip()
    elif '3' in voltar[0]:
        clear()
        print(f'{vd}Saindo...')
        exit()
    else:
        print(f'{ve}Comando não identificado')
        sleep(2)
        clear()
