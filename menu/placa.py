from menu.ascii import *
from menu.tools import *
import requests
import json


def cplaca():
    print(alpainel)
    placa = str(input(f'{am}Placa: {br}')).lower()
    info = requests.get(f'https://apicarros.com/v1/consulta/{placa}/json', verify=False).text
    info = json.loads(info)
    if 'uf' in placa:
        estado = requests.get(f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/' + info['uf'])
        estado = json.loads(estado.text)
        clear()
        print(alpainel)
        if 'LIMITE' in info:
            print(f'{ve}Limite de consulta atingido')
        else:
            print(f'''{am}Ano: {vd}{info['ano']}
{am}Ano modelo: {vd}{info['anoModelo']}
{am}Marca: {vd}{info['marca']}
{am}Cor: {vd}{info['cor']}
{am}Placa:  {vd}{info['placa']}
{am}Estado: {vd}{estado['nome']} ➤ {info['uf']}
{am}Cidade: {vd}{info['municipio']}
            ''')
        print(f'{ve}━' * 43)
        print(f'{am}[1] {cy}Menu\n'
              f'{am}[2] {cy}Consultar novamente\n'
              f'{am}[3] {cy}Sair')
        voltar = str(input(f'{am}//: {vd}'))
        if '1' in voltar[0]:
            clear()
        elif '2' in voltar[0]:
            clear()
            cplaca()
        elif '3' in voltar[0]:
            clear()
            print(f'{vd}Saindo...')
            exit()
        else:
            print(f'{ve}Comando não identificado')
            sleep(2)
            clear()
    else:
        print(f'{ve}Placa não identificada')
        sleep(2)
        clear()
        cplaca()
