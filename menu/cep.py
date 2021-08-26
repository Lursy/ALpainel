from menu.ascii import *
from menu.tools import *
import requests
import json


def ccep():
    print(alpainel)
    cep = str(input(f'{am}CEP: {vd}').strip())
    if len(cep) > 8:
        for c in range(len(cep), 8, -1):
            cep = cep[:-1]
    for c in range(len(cep), 8):
        cep = f'{cep + "0"}'
    if cep.isnumeric():
        dcep = json.loads(requests.get(f'https://viacep.com.br/ws/{cep}/json/').text)
        if 'erro' not in dcep:
            estado = requests.get(f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/' + dcep['uf'])
            estado = json.loads(estado.text)
            clear()
            print(alpainel)
            print(f'{vd}CEP:{am} {cep}\n'
                  f'{vd}Estado:{am} {dcep["uf"]}{br} ➤ {am}{estado["nome"]}\n'
                  f'{vd}Cidade:{am} {dcep["localidade"]}')
            if dcep['bairro'] != '':
                print(f'{vd}Bairro:{am} {dcep["bairro"]}')
            if dcep['logradouro'] != '':
                print(f'{vd}Rua:{am} {dcep["logradouro"]}')
            print(f'{vd}DDD:{am} {dcep["ddd"]}\033[m\n')
            print(f'{ve}━' * 43)
            print(f'{am}[1] {cy}Menu\n'
                  f'{am}[2] {cy}Consultar novamente\n'
                  f'{am}[3] {cy}Sair\n')
            voltar = str(input(f'{am}//: {vd}'))
            if '1' in voltar[0]:
                clear()
            elif '2' in voltar[0]:
                clear()
                ccep()
            elif '3' in voltar[0]:
                clear()
                print(f'{vd}Saindo...')
                exit()
            else:
                print(f'{ve}Comando não identificado')
                sleep(2)
                clear()
        else:
            print(f'{ve}O cep digitado não existe')
            sleep(2)
            clear()
            ccep()
    else:
        print(f'{ve}Cep não suportado')
        sleep(2)
        clear()
        ccep()
