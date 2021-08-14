#  os
try:
    import os
except ModuleNotFoundError:
    print('Error: Biblioteca "os" não instalada')
    print('Instalação manual')
    print('''1: python3 -m pip install --upgrade pip
2: pip install os''')


# threading
try:
    from threading import Thread
except ModuleNotFoundError:
    os.system('python3 -m pip install --upgrade pip')
    os.system('pip install threading')
    import threading


#  time
try:
    from time import sleep
except ModuleNotFoundError:
    os.system('python3 -m pip install --upgrade pip')
    os.system('pip install time')
    from time import sleep


#  json
try:
    import json
except ModuleNotFoundError:
    os.system('python3 -m pip install --upgrade pip')
    os.system('pip install json')
    import json


#  requests
try:
    import requests
except ModuleNotFoundError:
    os.system('python3 -m pip install --upgrade pip')
    os.system('pip install requests')
    import requests


# cores
ve = '\033[1;31m'  # Vermelho
vd = '\033[1;32m'  # Verde
am = '\033[1;33m'  # Amarelo
az = '\033[1;34m'  # Azul
br = '\033[1;37m'  # Branco
cy = '\033[1;36m'  # Ciano
rx = '\033[0;35m'  # Roxo
pt = '\033[0;40m'  # Fundo Preto
fv = '\033[0;42m'  # Fundo Verde
P = D = S = False


# strings
alpainel = f'''{rx}    _    _                 _            _
   / \  | |    _ __   __ _(_)_ __   ___| |
  / _ \ | |   | '_ \ / _` | | '_ \ / _ \ |
 / ___ \| |___| |_) | (_| | | | | |  __/ |
/_/   \_\_____| .__/ \__,_|_|_| |_|\___|_|
              |_| {cy}0.8{ve}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'''
painel = f'''{am}﴾ 1 ﴿{br}  ➤{vd}  CNPJ{ve}
━━━━━━━━━━━━━━━━━━━━━━━━
{am}﴾ 2 ﴿{br}  ➤{vd}  CEP{ve}
━━━━━━━━━━━━━━━━━━━━━━━━
{am}﴾ 3 ﴿{br}  ➤{vd}  Meu IP{ve}
━━━━━━━━━━━━━━━━━━━━━━━━
{am}﴾ 4 ﴿{br}  ➤{vd}  IP{ve}
━━━━━━━━━━━━━━━━━━━━━━━━
{am}﴾ 5 ﴿{br}  ➤  Root checker {ve}
━━━━━━━━━━━━━━━━━━━━━━━━
{am}﴾ 6 ﴿{br}  ➤  Meu canal{ve}
━━━━━━━━━━━━━━━━━━━━━━━━
{am}﴾ 7 ﴿{br}  ➤  Sair{ve}
━━━━━━━━━━━━━━━━━━━━━━━━'''


def clear():
    sleep(1)
    os.system('clear' if os.name != 'nt' else 'cls')


def ccep():
    print(alpainel)
    cep = str(input(f'{am}CEP: {vd}').strip())
    if len(cep) > 8:
        for c in range(len(cep), 8, -1):
            cep = cep[:-1]
    for c in range(len(cep), 8):
        cep = f'{cep + "0"}'
    dcep = json.loads(requests.get(f'https://viacep.com.br/ws/{cep}/json/').text)
    if 'erro' not in dcep:
        estado = requests.get(f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/' + dcep['uf'])
        estado = json.loads(estado.text)
        clear()
        print(alpainel)
        print(f'{pt}{vd}CEP:{am} {cep}\033[m\n'
              f'{pt}{vd}Estado:{am} {dcep["uf"]}{br} ➤ {am}{estado["nome"]}\033[m\n'
              f'{pt}{vd}Cidade:{am} {dcep["localidade"]}\033[m')
        if dcep['bairro'] != '':
            print(f'{pt}{vd}Bairro:{am} {dcep["bairro"]}\033[m')
        if dcep['logradouro'] != '':
            print(f'{pt}{vd}Rua:{am} {dcep["logradouro"]}\033[m')
        print(f'{pt}{vd}DDD:{am} {dcep["ddd"]}\033[m\n')
        voltar = str(input(f'{am}Voltar{cy}[S/N]: {vd}')).lower()
        if 's' in voltar[0]:
            clear()
            ccep()
        elif 'n' in voltar[0]:
            clear()
    else:
        print(f'{ve}O cep digitado não existe')
        sleep(2)
        clear()
        ccep()


def mip():
    print(alpainel)
    req = requests.get('https://www.meuip.com.br/').text
    a = req.find('Meu ip é')
    b = req.find('</h3>')
    c = req[a + 9:b]
    d = requests.get(f'http://ip-api.com/json/{c}').text
    ret = json.loads(d)
    print(f'{pt}{vd}IP atual:{am} {c}\033[m\n'
          f'{pt}{vd}Pais:{am} {ret["countryCode"]} {br}➤{am} {ret["country"]}\033[m\n'
          f'{pt}{vd}Cidade: {am}{ret["city"]}\033[m\n'
          f'{pt}{vd}Latitude:{am} {ret["lat"]}\033[m\n'
          f'{pt}{vd}Longitude:{am} {ret["lon"]}\033[m\n')
    voltar = str(input(f'{am}Voltar{cy}[S/N]: {vd}')).lower()
    if 's' in voltar[0]:
        clear()
        mip()
    elif 'n' in voltar[0]:
        clear()


def cip():
    print(alpainel)
    ip = str(input(f'{am}IP: {vd}'))
    if '.' in ip:
        d = requests.get(f'http://ip-api.com/json/{ip}')
        ret = json.loads(d.text)
        if f'""status":"fail"' in d:
            print(f'{ve}O ip digitado não existe ou foi escrito incorretamente!')
            sleep(2)
            clear()
            cip()
        clear()
        print(alpainel)
        print(f'{pt}{vd}IP: {am}{ip}\033[m\n'
              f'{pt}{vd}Pais:{am} {ret["countryCode"]} {br}➤{am} {ret["country"]}\033[m\n'
              f'{pt}{vd}Cidade: {am}{ret["city"]}\033[m\n'
              f'{pt}{vd}Latitude:{am} {ret["lat"]}\033[m\n'
              f'{pt}{vd}Longitude:{am} {ret["lon"]}\033[m\n')
        voltar = str(input(f'{am}Voltar{cy}[S/N]: {vd}')).lower()
        if 's' in voltar[0]:
            clear()
            cip()
        elif 'n' in voltar[0]:
            clear()
    else:
        print(f'{ve}Use a pontuação no IP')
        sleep(1)
        clear()
        cip()


def ccnpj():
    print(alpainel)
    cnpj = str(input(f'{am}CNPJ: ').replace('/', '').replace('.', '').replace('-', ''))
    clear()
    print(alpainel)
    inf = json.loads(requests.get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj}').text)
    print(f'{ve}DONO')
    print(f'{ve}━' * 30)
    if len(inf['qsa']) > 1:
        for c in range(0, len(inf['qsa'])):
            print(f"{am}{inf['qsa'][c]['qual']}\n{vd}{inf['qsa'][c]['nome']}")
    else:
        z = f"{inf['nome']}".find('1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9')
        print(f"{am}Nome: {vd}{inf['nome'][:z]}")
        print(f"{am}CPF:{vd} {inf['nome'][z:z+11]}")
    print(f'{ve}━' * 30)
    estado = json.loads(requests.get(f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{inf["uf"]}').text)
    print(f'\n{ve}ENDEREÇO')
    print(f'{ve}━' * 30)
    print(f'{am}cep:{vd}', inf['cep'])
    print(f'{am}Estado:{vd}', estado['nome'])
    print(f'{am}Cidade:{vd}', inf['municipio'])
    print(f'{am}Bairro:{vd}', inf['bairro'])
    print(f'{am}Rua:{vd}', inf['logradouro'])
    print(f'{am}Número:{vd}', inf['numero'])
    print(f'{ve}━' * 30)
    print(f'\n{ve}{inf["porte"]}')
    print(f'{ve}━' * 40)
    print(f"{am}Nome:{vd} {inf['fantasia']}")
    print(f'{am}Capital:{vd} {inf["capital_social"]}')
    print(f'{am}Abertura:{vd} {inf["abertura"]}')
    print(f'{am}Telefone:{vd} {inf["telefone"]}'.replace('/', ''))
    print(f'{am}Email:{vd} {inf["email"]}')
    print(f'{am}CNPJ:{vd} {inf["cnpj"]}')
    print(f'{ve}━' * 40)
    voltar = str(input(f'{am}Voltar{cy}[S/N]: {vd}')).lower()
    if 's' in voltar[0]:
        clear()
        ccnpj()
    elif 'n' in voltar[0]:
        clear()


try:
    clear()
    print(f'''{ve}                 ___====-_  _-====___
           _--^^^#####/./      \.\#####^^^--_
        _-^##########/./ (    ) \.\##########^-_
       -############/./  |\^^/|  \.\############-
     _/############/./   (@::@)   \.\############\_
    /#############(.(     \  /     ).)#############\,
   -###############\.\    (oo)    /./###############-
  -#################\.\  / VV \  /./#################-
 -###################\.\/      \/./###################-
  _#/|##########/\######(   /\   )######/\##########|\#_
  |/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|
  `  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '
     `   `  `      `   / | |  | | \   '      '  '   '
                      (  | |  | |  )
                     __\ | |  | | /__
                    (vvv(VVV)(VVV)vvv)
                      ASMODEUS&LURSY''')
    sleep(2)
    clear()
    while True:
        print(alpainel)
        print(painel)
        esc = int(input(f'{am}//: '))
        if esc == 1:
            clear()
            ccnpj()
        elif esc == 2:
            clear()
            ccep()
        elif esc == 3:
            clear()
            mip()
        elif esc == 4:
            clear()
            cip()
        elif esc == 5:
            root = os.system('su and exit')
            clear()
            print(alpainel)
            print(painel)
            if root == 0:
                print(f'{vd}Root ON')
            elif root == 256:
                print(f'{ve}Root OFF')
            else:
                print(f'{cy}Error')
            sleep(3)
            clear()
        elif esc == 6:
            os.system(f'termux-open-url https://www.youtube.com/channel/UCwmkiKIZHL1wscYHfIINZKw')
            clear()
        elif esc == 7:
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
