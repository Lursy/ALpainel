from LPainel import *
from time import sleep


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
