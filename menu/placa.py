from menu.ascii import *
from menu.tools import *
import requests
import json


def cplaca():
    print(alpainel)
    placa = str(input(f'{am}Placa: {br}')).lower()
    info = requests.get(f'https://apicarros.com/v1/consulta/{placa}/json', verify=False).text
    info = json.loads(info)
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
    voltar = str(input(f'{am}Voltar{cy}[S/N]: {vd}')).lower()
    if 's' in voltar[0]:
        clear()
        cplaca()
    elif 'n' in voltar[0]:
        clear()
