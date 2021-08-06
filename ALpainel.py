#  Modulos
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
sex = data = ''
filtros = fdata = fsexo = pronto = fil = ''
inicial = f'''{vd}┏━━━━━━━━━━━━━━━━━┓
┃ {am}[1]›{cy} Filtros{vd}    ┃
┣━━━━━━━━━━━━━━━━━┫
┃ {am}[2]›{cy} Continuar{vd}  ┃
┣━━━━━━━━━━━━━━━━━┫
┃ {am}[3]›{cy} Sair{vd}       ┃
┗━━━━━━━━━━━━━━━━━┛'''
alpainel = f'''{rx}    _    _                 _            _
   / \  | |    _ __   __ _(_)_ __   ___| |
  / _ \ | |   | '_ \ / _` | | '_ \ / _ \ |
 / ___ \| |___| |_) | (_| | | | | |  __/ |
/_/   \_\_____| .__/ \__,_|_|_| |_|\___|_|
              |_| {cy}0.8{br}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'''
painel = f'''{am}﴾ 1 ﴿{br}  ➤{vd}  Nome{br}
━━━━━━━━━━━━━━━━━━━━
{am}﴾ 2 ﴿{br}  ➤{ve}  CNPJ{br}
━━━━━━━━━━━━━━━━━━━━
{am}﴾ 3 ﴿{br}  ➤{ve}  CPF{br}
━━━━━━━━━━━━━━━━━━━━
{am}﴾ 4 ﴿{br}  ➤{vd}  CEP{br}
━━━━━━━━━━━━━━━━━━━━
{am}﴾ 5 ﴿{br}  ➤{vd}  Meu IP{br}
━━━━━━━━━━━━━━━━━━━━
{am}﴾ 6 ﴿{br}  ➤{vd}  IP{br} 
━━━━━━━━━━━━━━━━━━━━
{am}﴾ 7 ﴿{br}  ➤  Creditos
━━━━━━━━━━━━━━━━━━━━
{am}﴾ 8 ﴿{br}  ➤  Sair 
━━━━━━━━━━━━━━━━━━━━'''


def menu():
    clear()
    global fdata, fsexo, filtros, pronto, fil
    print(alpainel)
    filtros = f'''{vd}┏› {rx}Filtros{vd}  ‹┓
┣━━━━━━━━━━━━┫\n'''
    if not D:
        fdata = f'''{vd}┃ {am}[D]›{cy}Data{vd}   ┃
┣━━━━━━━━━━━━┫\n'''
    else:
        fdata = ''
    if not S:
        fsexo = f'''{vd}┃ {am}[S]›{cy}Sexo{vd}   ┃
┣━━━━━━━━━━━━┫\n'''
    else:
        fsexo = ''
    if P:
        pronto = f'''{vd}┃ {am}[P]›{cy}Pronto{vd} ┃
┗━━━━━━━━━━━━┛\n'''
    else:
        pronto = f'''{vd}┃ {am}[V]›{cy}Voltar{vd} ┃
┗━━━━━━━━━━━━┛'''
    fmenu = f'{filtros}{fdata}{fsexo}{pronto}'
    print(fmenu)
    fil = str(input(f'{am}//: {br}').upper())
    if fil[0] == 'D' and not D:
        datan()
    elif fil[0] == 'S' and not S:
        sexon()
    elif fil[0] == 'P' and P:
        pass
    elif fil[0] == 'V' and P:
        cnome()
    else:
        print(f'{ve}Comando inválido!')
        sleep(1)
        clear()
        cnome()


def datan():
    clear()
    global data, D, P
    print(alpainel)
    data = str(input(f'{cy}[DIA/MÊS/ANO] ou somente [ANO]: {vd}').rstrip(']').replace('[', ''))
    if len(data) == 8:
        data = f'{data[:2]}/{data[2:4]}/{data[4:8]}'
    elif len(data) == 4:
        data = f'/{data}'
    elif len(data) == 10:
        pass
    else:
        print(f'{ve}Data inválida!')
        sleep(1)
        cnome()
    D = P = True
    menu()


def sexon():
    clear()
    global sex, S, P
    print(alpainel)
    print(f'''{vd}┏›     {rx}Sexo{vd}      ‹┓
┣━━━━━━━━━━━━━━━━━┫
┃ {am}[1]›{cy} Masculino{vd}  ┃
┣━━━━━━━━━━━━━━━━━┫
┃ {am}[2]›{cy} Feminino{vd}   ┃
┣━━━━━━━━━━━━━━━━━┫
┃ {am}[3]›{cy} Intersexo{vd}  ┃
┗━━━━━━━━━━━━━━━━━┛''')
    sexo = str(input(f'{cy}Sexo: {vd}')).lower()
    if sexo == '1' or sexo[0] == 'm':
        sex = 'Masculino'
    elif sexo == '2' or sexo[0] == 'f':
        sex = 'Feminino'
    elif sexo == '3' or sexo[0] == 'i':
        sex = 'Intersexo'
    else:
        print(f'{ve}Comando inválido')
        sleep(1)
        cnome()
    S = P = True
    menu()


def loading():
    print(f'{vd}Loading...\033[m', end='')
    for c in range(0, 10):
        sleep(0.1)
        print(f'{fv}\033[m' if c == 0 else f'{fv}ㅤ\033[m' * c)


def clear():
    sleep(1)
    os.system('clear' if os.name != 'nt' else 'cls')


def ccep():
    estado = {'nome': ''}
    req = ''
    print(alpainel)
    cep = str(input(f'{am}CEP: {vd}').strip())
    if len(cep) > 8:
        for c in range(len(cep), 8, -1):
            cep = cep[:-1]
    for c in range(len(cep), 8):
        cep = f'{cep + "0"}'
    try:
        req = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    except:
        print(f'{ve}Conecte-se para que possa usar a script')
        sleep(2)
        clear()
        exit()
    try:
        dcep = json.loads(req.text)
        if 'erro' in dcep:
            print(f'{ve}O cep digitado não existe')
            sleep(2)
            clear()
            ccep()
        try:
            estado = requests.get(f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{dcep["uf"]}')
        except:
            print(f'{ve}Conecte-se para que possa usar a script')
            sleep(2)
            clear()
            exit()
        estado = json.loads(estado.text)
        clear()
        print(alpainel)
        print(f'{pt}{vd}CEP:{am} {cep}\033[m')
        print(f'{pt}{vd}Estado:{am}', f'{dcep["uf"]}{br} ➤ {am}{estado["nome"]}\033[m')
        print(f'{pt}{vd}Cidade:{am} {dcep["localidade"]}\033[m')
        if dcep['bairro'] != '':
            print(f'{pt}{vd}Bairro:{am} {dcep["bairro"]}\033[m')
        if dcep['logradouro'] != '':
            print(f'{pt}{vd}Rua:{am} {dcep["logradouro"]}\033[m')
        print(f'{pt}{vd}DDD:{am} {dcep["ddd"]}\033[m\n')
    except:
        print(f'{ve}CEP digitado não existe')
        clear()
        ccep()
    A = str(input(f'{am}Voltar{cy}[S/N]: {vd}')).lower()
    if 's' in A[0]:
        clear()
        pass
    elif 'n' in A[0]:
        print(f'{vd}Saindo...')
        exit()


def cnome():
    r = ''
    print(alpainel)
    global data, fil, sex, P, D, S
    sex = data = ' '
    P = D = S = False
    nome = input(f'{am}Nome: {vd}')
    load = Thread(target=loading)
    load.start()
    try:
        r = requests.get(
            url='https://consulta-nome1.p.rapidapi.com/apis/astrahvhdeus/Consultas%20Privadas/HTML/nome.php',
            headers={
                'User-Agent':
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
                'x-rapidapi-key': 'e01238c690msh74f20bdc84d5dcfp122562jsnc9921fa7c4c1',
                'x-rapidapi-host': 'consulta-nome1.p.rapidapi.com'},
            params={'consulta': nome}).text
    except:
        print(f'{ve}Conecte-se para que possa usar a script')
        sleep(2)
        clear()
        exit()
    print(f'{fv}ㅤ\033[m' * 10)
    print(f'{vd}Concluido!')
    clear()
    print(alpainel)
    print(inicial)
    try:
        fil = int(input(f'{am}//: {br}'))
    except ValueError:
        print(f'{ve}Use apenas números')
        sleep(1)
        cnome()
    if fil == 1:
        menu()
        clear()
        print(f'{alpainel}', end='')
    elif fil == 2:
        clear()
        print(f'{alpainel}', end='')
        pass
    elif fil == 3:
        clear()
        exit()
    else:
        print(f'{ve}Comando inválido')
        sleep(1)
        clear()
        cnome()
    r = r.replace('\\', '/') \
        .replace('<br>', '!!\n') \
        .replace('CPF:', f'{pt}{vd}<CPF: {am}') \
        .replace('NOME:', f'{pt}{vd}Nome: {am}') \
        .replace('SEXO:', f'{pt}{vd}Sexo: {am}') \
        .replace('M - Masculino', 'Masculino') \
        .replace('F - Feminino', 'Feminino') \
        .replace('NASCIMENTO:', f'{pt}{vd}Nascimento: {am}') \
        .replace('!!', '\033[m') \
        .replace('/r<p>', '>\033[m^~/!') \
        .replace('I - Intersexo', 'Intersexo')
    if data and sex in r:
        r = r.replace('^~/!', '')
        cont = 0
        q = r.count('>')
        for c in range(0, q):
            ini = r.find('<')
            fim = r.find('>')
            if f'{data}' in r[(ini + 30):(fim + 35)] and sex in r[(ini + 30):(fim + 35)]:
                r2 = r[(ini - 15):(fim + 4)]
                inf = r2.replace('>', '').replace('<', '')
                print(inf)
                print(f'\033[m━' * 40, end='')
                sleep(0.4)
                cont += 1
            r = r[(fim + 4):]
        print('\n')
        A = str(input(f'{am}Voltar{cy}[S/N]: {vd}')).lower()
        if 's' in A[0]:
            clear()
            pass
        elif 'n' in A[0]:
            print(f'{vd}Saindo...')
            exit()
    elif 'Sobrenome' in r:
        print(f'{ve}Utilize sobrenomes nas consultas!')
        sleep(2)
        cnome()
    elif D and S:
        D = f'{data}'
        if D not in r:
            print(f'{ve}\nNenhum nome foi encontrado em {data[1:]}')
            sleep(2)
            cnome()
        else:
            print(f'{ve}\nNão foram encontradas pessoas do sexo {sex}')
            sleep(2)
            cnome()
    else:
        print(f"{ve}Não encotramos ninguém :'(")
        sleep(2)
        cnome()


def mip():
    req = d = ''
    print(alpainel)
    try:
        req = requests.get('https://www.meuip.com.br/').text
    except:
        print(f'{ve}Conecte-se para que possa usar a script')
        sleep(2)
        clear()
        exit()
    a = req.find('Meu ip é')
    b = req.find('</h3>')
    c = req[a + 9:b]
    try:
        d = requests.get(f'http://ip-api.com/json/{c}').text
    except:
        print(f'{ve}Conecte-se para que possa usar a script')
        sleep(2)
        clear()
        exit()
    ret = json.loads(d)
    print(f'{pt}{vd}IP atual:{am} {c}\033[m')
    print(f'{pt}{vd}Pais:{am}', ret['countryCode'], f'{br}➤{am} {ret["country"]}\033[m')
    print(f'{pt}{vd}Cidade: {am}{ret["city"]}\033[m')
    print(f'{pt}{vd}Latitude:{am} {ret["lat"]}\033[m')
    print(f'{pt}{vd}Longitude:{am} {ret["lon"]}\033[m\n')
    A = str(input(f'{am}Voltar{cy}[S/N]: {vd}')).lower()
    if 's' in A[0]:
        clear()
        pass
    elif 'n' in A[0]:
        print(f'{vd}Saindo...')
        exit()


def cip():
    d = ''
    print(alpainel)
    ip = str(input(f'{am}IP: {vd}'))
    if '.' in ip:
        pass
    else:
        print(f'{ve}Use a pontuação no IP')
        sleep(1)
        clear()
        cip()
    try:
        d = requests.get(f'http://ip-api.com/json/{ip}')
    except:
        print(f'{ve}Conecte-se para que possa usar a script')
        sleep(2)
        clear()
        exit()
    ret = json.loads(d.text)
    if 'invalid query' in ret["message"]:
        print(f'{ve}O ip digitado não existe ou foi escrito incorretamente!')
        sleep(2)
        clear()
        cip()
    clear()
    print(alpainel)
    print(f'{pt}{vd}IP: {am}{ip}\033[m')
    print(f'{pt}{vd}Pais:{am}', ret['countryCode'], f'{br}➤{am} {ret["country"]}\033[m')
    print(f'{pt}{vd}Cidade: {am}{ret["city"]}\033[m')
    print(f'{pt}{vd}Latitude:{am} {ret["lat"]}\033[m')
    print(f'{pt}{vd}Longitude:{am} {ret["lon"]}\033[m\n')
    A = str(input(f'{am}Voltar{cy}[S/N]: {vd}')).lower()
    if 's' in A[0]:
        clear()
        pass
    elif 'n' in A[0]:
        print(f'{vd}Saindo...')
        exit()


try:
    clear()
    print(f'''{ve}Façam o que bem entenderem, isso não é problema meu.''')
    sleep(2)
    clear()
    while True:
        print(alpainel)
        print(painel)
        esc = int(input(f'{am}//: '))
        if esc == 1:
            clear()
            cnome()
        elif esc == 2:
            print(f'{ve}Em produção')
            sleep(1)
            clear()
        elif esc == 3:
            print(f'{ve}Em produção')
            sleep(1)
            clear()
        elif esc == 4:
            clear()
            ccep()
        elif esc == 5:
            clear()
            mip()
        elif esc == 6:
            clear()
            cip()
        elif esc == 7:
            clear()
            print(alpainel)
            print(f'{br}Criação:{cy} Lursy')
            sleep(1)
            print(f'{br}API nome: {cy}Kiny')
            sleep(1)
            clear()
        elif esc == 8:
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
