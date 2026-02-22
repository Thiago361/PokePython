import time
import os
import random
import msvcrt
import copy

from infos_pokemons import pokemons, inimigos
from animation import animated_ascii_typing
from battle_screens import telaDerrota, telaVitoria
from battle_texts import frases_aproximacao, frases_surgimento
from battle_logic import atacarPokemon, foiAtacadoPokemon, verificarMorte
from utils import timeCls

def pokeEscolhido(escolha):
    return pokemons.get(escolha)
    
def lutaPokePythonLoop(PokemonEscolhido, inimigoEscolhido):
    while True:
        print('\nQual move você escolhe?\n')
        for chave, ataque in PokemonEscolhido["ataques"].items():
            print(f'{chave} - {ataque["nome"]} -> ATK: {ataque["dano"]} / PP -> {ataque["pp"]}')
            
        ChooseMove = input('')
        if ChooseMove in PokemonEscolhido['ataques']:
        
            timeCls(0, 'cls')
            
            ChooseMoveAtk = PokemonEscolhido["ataques"][ChooseMove]
            if ChooseMoveAtk['pp'] > 0:
                atacarPokemon(ChooseMove,PokemonEscolhido, inimigoEscolhido)
                verificarVitoria = verificarMorte(PokemonEscolhido, inimigoEscolhido)
                if verificarVitoria == "inimigo_morto":
                    if telaVitoria():
                        jogarNovamente()
                    else:
                        break
                foiAtacadoPokemon(PokemonEscolhido, inimigoEscolhido)
                verificarVitoria = verificarMorte(PokemonEscolhido, inimigoEscolhido)
                if verificarVitoria == "jogador_morto":
                    if telaDerrota():
                        jogarNovamente()
                    else:
                        break

            else:
                timeCls(0, 'cls')
                print("O pp desse ataque acabou, escolha outro")
        else:
            timeCls(0, 'cls')
            print('escolhe novamente marreco, esse ataque não existe...')
    
    
def iniciar_jogo():
    
    timeCls(0, 'cls')
    animated_ascii_typing()
    print('BEM VINDO AO POKÉPYTHON 😉☺️'.center(50))

    timeCls(4, 'cls')
    
    print("Olá! Eu sou o Professor PyOak! 🧪🐍")
    timeCls(1, 'n')
    print("Este mundo é habitado por criaturas chamadas PokéPython!\n")
    timeCls(1, 'n')
    nomeJogador = input("Mas antes de começarmos sua jornada...\nQual é o seu nome, jovem treinador? ")
    timeCls(1, 'cls')

    print(f"\n👋 Olá, {nomeJogador}!")
    
    print("Escolha seu PokéPython inicial:")
    for chave, dados in pokemons.items():
        print(f"[{chave}] - {dados['nome']}")

    while True:
        escolha = input("\nQual sua escolha? = ")

        PokemonEscolhido = copy.deepcopy(pokeEscolhido(escolha))
        if PokemonEscolhido:
            timeCls(0, 'cls')
        
            print(f"Você escolheu {PokemonEscolhido['nome']}!")
        
            timeCls(2, 'cls')
        
            print(f"{PokemonEscolhido['nome']} tem ❤️  {PokemonEscolhido['vida']} de vida")
            print(f"Ele tem 4 moves:")
        
            for chave, ataque in PokemonEscolhido["ataques"].items():
                print(f'{ataque["nome"]} -> ATK: {ataque["dano"]} / PP : {ataque["pp"]}')
            
            print("\nPressione qualquer tecla para começar...")
            msvcrt.getch()
            timeCls(0, 'cls')
            break
        else:
            os.system("cls")
            print("Escreve certinho pra mim 😠")
            for chave, dados in pokemons.items():
                print(f"[{chave}] - {dados['nome']}")
        
    inimigoAleatorio = random.choice(list(inimigos.values()))
    inimigoEscolhido = copy.deepcopy(inimigoAleatorio)
    
    print(f"\n🌪{random.choice(frases_aproximacao)}")
    timeCls(1, 'n')
    print("...")
    timeCls(1, 'n')
    print("...")
    timeCls(1, 'cls')
    print(f"💥 {inimigoEscolhido['nome']} {random.choice(frases_surgimento)}")
    print(f"❤️  Vida: {inimigoEscolhido['vida']}")
    print("Prepare-se para lutar! ⚔️\n")
    
    lutaPokePythonLoop(PokemonEscolhido, inimigoEscolhido)
    
def jogarNovamente():
    
    timeCls(0, 'cls')
    animated_ascii_typing()

    timeCls(4, 'cls')
    
    print("Escolha seu PokéPython:")
    for chave, dados in pokemons.items():
        print(f"[{chave}] - {dados['nome']}")

    while True:
        escolha = input("\nQual sua escolha? = ")

        PokemonEscolhido = copy.deepcopy(pokeEscolhido(escolha))
        if PokemonEscolhido:
            timeCls(0, 'cls')
        
            print(f"Você escolheu {PokemonEscolhido['nome']}!")
        
            timeCls(2, 'cls')
        
            print(f"{PokemonEscolhido['nome']} tem ❤️  {PokemonEscolhido['vida']} de vida")
            print(f"Ele tem 4 moves:")
        
            for chave, ataque in PokemonEscolhido["ataques"].items():
                print(f'{ataque["nome"]} -> ATK: {ataque["dano"]} / PP : {ataque["pp"]}')
            
            print("\nPressione qualquer tecla para começar...")
            msvcrt.getch()
            timeCls(0, 'cls')
            break
        else:
            os.system("cls")
            print("Escreve certinho pra mim 😠")
            for chave, dados in pokemons.items():
                print(f"[{chave}] - {dados['nome']}")
        
    inimigoAleatorio = random.choice(list(inimigos.values()))
    inimigoEscolhido = copy.deepcopy(inimigoAleatorio)
    
    print(f"\n🌪{random.choice(frases_aproximacao)}")
    timeCls(1, 'n')
    print("...")
    timeCls(1, 'n')
    print("...")
    timeCls(1, 'cls')
    print(f"💥 {inimigoEscolhido['nome']} {random.choice(frases_surgimento)}")
    print(f"❤️  Vida: {inimigoEscolhido['vida']}")
    print("Prepare-se para lutar! ⚔️\n")
    
    lutaPokePythonLoop(PokemonEscolhido, inimigoEscolhido)


if __name__ == "__main__":
    iniciar_jogo()




