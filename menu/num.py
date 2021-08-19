from menu.ascii import *
from menu.tools import *
import phonenumbers


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
