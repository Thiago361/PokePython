import sys
import os
import time
from colorama import Fore

def animated_ascii_typing():
    ascii_art = r"""
  ____   ___  _  _______ ______   _______ _   _  ___  _   _ 
 |  _ \ / _ \| |/ / ____|  _ \ \ / /_   _| | | |/ _ \| \ | |
 | |_) | | | | ' /|  _| | |_) \ V /  | | | |_| | | | |  \| |
 |  __/| |_| | . \| |___|  __/ | |   | | |  _  | |_| | |\  |
 |_|    \___/|_|\_\_____|_|    |_|   |_| |_| |_|\___/|_| \_|
    """

    print(Fore.MAGENTA)

    for char in ascii_art:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.002)

def animar_barra_vida(pokemon, dano):
    for _ in range(dano):
        if pokemon["vida"] > 0:
            pokemon["vida"] -= 1
        
        os.system('cls')
        print(f'{pokemon["nome"]}')
        print(f'❤️ {max(0, pokemon["vida"])} de vida')
        time.sleep(0.03)
