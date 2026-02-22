def mostrarVidaAtual( PokemonEscolhido, inimigoEscolhido):
    print(f' {PokemonEscolhido["nome"]}')
    if PokemonEscolhido["vida"] <= 0:
        PokemonEscolhido["vida"] = 0
    print(f'❤️ {PokemonEscolhido["vida"]} de vida')
    print('-' * 15)
    if inimigoEscolhido["vida"] <= 0: 
        inimigoEscolhido["vida"] = 0
    print(f' {inimigoEscolhido["nome"]}')
    print(f'❤️ {inimigoEscolhido["vida"]} de vida')
    
    
def telaVitoria():
    print("\n" + "="*40)
    print("🏆 PARABÉNS, TREINADOR!")
    print("Você venceu a batalha!")
    print("="*40)

    while True:
        escolha = input("\nDeseja jogar novamente? (s/n): ").lower()

        if escolha == "s":
            return True
        elif escolha == "n":
            print("\nObrigado por jogar PokéPython! 👋")
            return False
        else:
            print("Digite apenas 's' ou 'n'.")


def telaDerrota():
    print("\n" + "="*40)
    print("💀 SEU POKÉPYTHON FOI DERROTADO!")
    print("Você perdeu a batalha...")
    print("="*40)

    while True:
        escolha = input("\nDeseja tentar novamente? (s/n): ").lower()

        if escolha == "s":
            return True
        elif escolha == "n":
            print("\nTreinador recuou... Até a próxima! 👋")
            return False
        else:
            print("Digite apenas 's' ou 'n'.")