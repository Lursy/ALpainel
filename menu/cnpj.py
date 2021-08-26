from menu.ascii import *
from menu.tools import *
import requests
import json


def ccnpj():
    print(alpainel)
    cnpj = str(input(f'{am}CNPJ: ').replace('/', '').replace('.', '').replace('-', ''))
    clear()
    print(alpainel)
    inf = json.loads(requests.get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj}').text)
    if inf['status'] != 'ERROR':
        print(f'{ve}DONO')
        print(f'{ve}━' * 43)
        if len(inf['qsa']) > 1:
            for c in range(0, len(inf['qsa'])):
                print(f"{am}{inf['qsa'][c]['qual']}\n{vd}{inf['qsa'][c]['nome']}")
        else:
            z = f"{inf['nome']}".find('1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9')
            print(f"{am}Nome: {vd}{inf['nome'][:z]}")
            print(f"{am}CPF:{vd} {inf['nome'][z:z+11]}")
        print(f'{ve}━' * 43)
        estado = json.loads(
            requests.get(f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{inf["uf"]}').text
        )
        print(f'\n{ve}ENDEREÇO')
        print(f'{ve}━' * 43)
        print(f'{am}cep:{vd}', inf['cep'])
        print(f'{am}Estado:{vd}', estado['nome'])
        print(f'{am}Cidade:{vd}', inf['municipio'])
        print(f'{am}Bairro:{vd}', inf['bairro'])
        print(f'{am}Rua:{vd}', inf['logradouro'])
        print(f'{am}Número:{vd}', inf['numero'])
        print(f'{ve}━' * 43)
        print(f'\n{ve}{inf["porte"]}')
        print(f'{ve}━' * 43)
        print(f"{am}Nome:{vd} {inf['fantasia']}")
        print(f'{am}Capital:{vd} {inf["capital_social"]}')
        print(f'{am}Abertura:{vd} {inf["abertura"]}')
        print(f'{am}Telefone:{vd} {inf["telefone"]}'.replace('/', ''))
        print(f'{am}Email:{vd} {inf["email"]}')
        print(f'{am}CNPJ:{vd} {inf["cnpj"]}')
        print(f'{ve}━' * 43)
        print(f'{am}[1] {cy}Menu\n'
              f'{am}[2] {cy}Consultar novamente\n'
              f'{am}[3] {cy}Sair')
        voltar = str(input(f'{am}//: {vd}'))
        if '1' in voltar[0]:
            clear()
        elif '2' in voltar[0]:
            clear()
            ccnpj()
        elif '3' in voltar[0]:
            clear()
            print(f'{vd}Saindo...')
            exit()
        else:
            print(f'{ve}Comando não identificado')
            sleep(2)
            clear()
    else:
        print(f'{ve}{inf["message"]}')
        sleep(2)
        clear()
        ccnpj()
