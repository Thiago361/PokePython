import random
import msvcrt

from animation import animar_barra_vida
from battle_screens import mostrarVidaAtual
from battle_texts import frases_ataque
from utils import timeCls

def atacarPokemon(ChooseMove,PokemonEscolhido, inimigoEscolhido):
    vidaAtual = inimigoEscolhido['vida']
    ataqueUsado = PokemonEscolhido["ataques"][ChooseMove]["dano"]
    PpdoAtkUsado = PokemonEscolhido["ataques"][ChooseMove]["pp"]
    vidaAtual -= ataqueUsado
    inimigoEscolhido['vida'] = vidaAtual
    animar_barra_vida(inimigoEscolhido, PokemonEscolhido["ataques"][ChooseMove]["dano"])
    timeCls(0, 'cls')
    print(f'\nvocê atacou o {inimigoEscolhido["nome"]} com {PokemonEscolhido["ataques"][ChooseMove]["nome"]} e causou {ataqueUsado} de dano\n')
    mostrarVidaAtual(PokemonEscolhido, inimigoEscolhido)
    PpdoAtkUsado -= 1
    PokemonEscolhido["ataques"][ChooseMove]["pp"] = PpdoAtkUsado
    print("\nPressione qualquer tecla para continuar...")
    msvcrt.getch()
    
def foiAtacadoPokemon(PokemonEscolhido, inimigoEscolhido):
    timeCls(0, 'cls')
    fraseAtkInimiga = random.choice(frases_ataque)
    print(f'{fraseAtkInimiga}\n')
    timeCls(1,'n')
    ChooseMoveInimigo = str(random.randint(1,4))
    vidaAtual = PokemonEscolhido['vida']
    ataqueUsado = inimigoEscolhido["ataques"][ChooseMoveInimigo]["dano"]
    vidaAtual -= ataqueUsado
    PokemonEscolhido['vida'] = vidaAtual
    animar_barra_vida(PokemonEscolhido, inimigoEscolhido["ataques"][ChooseMoveInimigo]["dano"])
    timeCls(0, 'cls')
    print(f'{PokemonEscolhido["nome"]} foi atacado com {inimigoEscolhido["ataques"][ChooseMoveInimigo]["nome"]} e causou {ataqueUsado} de dano\n')
    mostrarVidaAtual(PokemonEscolhido, inimigoEscolhido)
    
def verificarMorte(PokemonEscolhido,inimigoEscolhido): 
    if PokemonEscolhido["vida"] <= 0:
        PokemonEscolhido["vida"] = 0
        return "jogador_morto" 
    elif inimigoEscolhido["vida"] <= 0:
        inimigoEscolhido["vida"] = 0
        return "inimigo_morto"