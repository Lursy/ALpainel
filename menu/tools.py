from time import sleep
import os

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

def clear():
    sleep(1)
    os.system('clear' if os.name != 'nt' else 'cls')
