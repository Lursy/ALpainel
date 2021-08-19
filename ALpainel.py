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


# cores
ve = '\033[1;31m'  # Vermelho
vd = '\033[1;32m'  # Verde
am = '\033[1;33m'  # Amarelo
az = '\033[1;34m'  # Azul
br = '\033[1;37m'  # Branco
cy = '\033[1;36m'  # Ciano
rx = '\033[0;35m'  # Roxo
pt = '\033[1;30m'  # Preto
fv = '\033[1;42m'  # Fundo verde
P = D = S = False


# strings
alpainel = f'''{rx}      _    _                 _            _
     / \  | |    _ __   __ _(_)_ __   ___| |
    / _ \ | |   | '_ \ / _` | | '_ \ / _ \ |
   / ___ \| |___| |_) | (_| | | | | |  __/ |
  /_/   \_\_____| .__/ \__,_|_|_| |_|\___|_|
                |_| {cy}2.0{ve}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n'''
painel = f'''{ve}┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃    {am}[{vd} CONSULTAS {am}]{ve}     ┃  {am}[{az} Ferramentas {am}]{ve}   ┃
┃
┣┫{am}[1]{vd} Consulta CNPJ{ve}  ◄━╋┫{am}[5]{az} Info número{ve}  ◄━┫
┃
┣┫{am}[2]{vd} Consulta CEP{ve}   ◄━╋┫{am}[6]{az} Root checker{ve} ◄━┫
┃
┣┫{am}[3]{vd} Consulta IP{ve}    ◄━╋┫{am}[7]{az} Meu IP{ve}       ◄━┫
┃
┣┫{am}[4]{vd} Consulta Placa{ve} ◄━╋━━━━━━━━━━━━┳━━━━━━━┛
┃                      ┃ {am}[{br} Opções {am}]{ve} ┃
┗━━━━━━━━━━━━━━━━━━┳━━━┛
                   ┣┫{am}[8]{br} Criador{ve}  ◄━┫
                   ┃
                   ┣┫{am}[9]{br} Sair{ve}     ◄━┫
                   ┗━━━━━━━━━━━━━━━━┻Lursy'''


def clear():
    sleep(1)
    os.system('clear' if os.name != 'nt' else 'cls')


def numeros():
    EUA = 'n'
    print(alpainel)
    telefone = str(input(f'{am}Número: {br}'))
    ps = len(telefone)
    if ps == 11 and not '+' in telefone:
        EUA = str(input(f'{am}O número inserido é internacional?{cy}[S/N] ')[0].lower())
    if EUA == 's' or EUA == 'n':
        num = phonenumbers.parse(f'+{telefone.replace("+", "")}'
                                 if ps > 12 or EUA == 's' or '+' in telefone else
                                 telefone, 'BR')
        numero = phonenumbers.format_number(num, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        clear()
        print(alpainel)
        print(f'{vd}[+]{am}Número: {vd}' + numero)
        sleep(0.5)
        from phonenumbers import carrier, geocoder
        pais = geocoder.country_name_for_number(num, 'pt')
        print(f'{vd}[+]{am}Pais: {vd}' + pais if pais != '' else f'{ve}[-]{am}Pais: {vd}None')
        sleep(0.5)
        estado = geocoder.description_for_number(num, 'pt-br')
        print(f'{vd}[+]{am}Estado: {vd}' + estado if estado != '' else f'{ve}[-]{am}Estado: {vd}None')
        sleep(0.5)
        operadora = carrier.name_for_number(num, 'en')
        print(f'{vd}[+]{am}Operadora: {vd}' + operadora if operadora != '' else f'{ve}[-]{am}Operadora: {vd}None\n')
        sleep(0.5)
        print(f'{ve}━' * 43)
        voltar = str(input(f'{am}Voltar{cy}[S/N]: {vd}')).lower()
        if 's' in voltar[0]:
            clear()
            numeros()
        elif 'n' in voltar[0]:
            clear()
    else:
        print(f'{ve}Comando inválido!')
        sleep(2)
        clear()
        numeros()


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
        ccnpj()
    elif 'n' in voltar[0]:
        clear()


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
        print(f'{vd}CEP:{am} {cep}\n'
              f'{vd}Estado:{am} {dcep["uf"]}{br} ➤ {am}{estado["nome"]}\n'
              f'{vd}Cidade:{am} {dcep["localidade"]}')
        if dcep['bairro'] != '':
            print(f'{vd}Bairro:{am} {dcep["bairro"]}')
        if dcep['logradouro'] != '':
            print(f'{vd}Rua:{am} {dcep["logradouro"]}')
        print(f'{vd}DDD:{am} {dcep["ddd"]}\033[m\n')
        print(f'{ve}━' * 43)
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
    print(f'{vd}IP atual:{am} {c}\n'
          f'{vd}Pais:{am} {ret["countryCode"]} {br}➤{am} {ret["country"]}\n'
          f'{vd}Cidade: {am}{ret["city"]}\n'
          f'{vd}Latitude:{am} {ret["lat"]}\n'
          f'{vd}Longitude:{am} {ret["lon"]}\n')
    print(f'{ve}━' * 43)
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
        print(f'{vd}IP: {am}{ip}\033[m\n'
              f'{vd}Pais:{am} {ret["countryCode"]} {br}➤{am} {ret["country"]}\n'
              f'{vd}Cidade: {am}{ret["city"]}\n'
              f'{vd}Latitude:{am} {ret["lat"]}\n'
              f'{vd}Longitude:{am} {ret["lon"]}\n')
        print(f'{ve}━' * 43)
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
    print(f'''{ve}                  ___====-_  _-====___
            _--^^^#####/./      \.\#####^^^--_
         _-^##########/./ (    ) \.\##########^-_
        -############/./  |\^^/|  \.\############-
      _/############/./   (@::@)   \.\############\_
     /#############(.(     \  /     ).)#############\,
    -###############\.\    (oo)    /./###############-
   -#################\.\  / VV \  /./#################-
  -###################\.\/      \/./###################-
  _#/|##########/\#####(    /\    )#####/\##########|\#_
  |/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|
  `  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '
     `   `  `      `   / | |  | | \   '      '  '   '
                      (  | |  | |  )
                     __\ | |  | | /__
                    (vvv(VVV)(VVV)vvv)''')
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
            cip()
        elif esc == 4:
            clear()
            cplaca()
        elif esc == 5:
            clear()
            numeros()
        elif esc == 6:
            root = os.system('su and exit>null')
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
            mip()
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
