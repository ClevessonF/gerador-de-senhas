import random
import string


def gerar_senha(tamanho=12, usar_maiusculas=True, usar_numeros=True, usar_simbolos=True):
    """Gera uma senha aleatória com base nos parâmetros informados."""
    caracteres = string.ascii_lowercase

    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    return "".join(random.choice(caracteres) for _ in range(tamanho))


def escolher_tamanho():
    """Mostra um mini menu para o usuário escolher o tamanho da senha."""
    print("=" * 40)
    print("      GERADOR DE SENHAS - MENU")
    print("=" * 40)
    print("Quantos caracteres você quer na senha?")
    print("  1 - 8 caracteres")
    print("  2 - 12 caracteres")
    print("  3 - 16 caracteres")
    print("  4 - Escolher outro tamanho")
    print("=" * 40)

    escolha = input("Digite o número da opção: ").strip()

    opcoes = {"1": 8, "2": 12, "3": 16}

    if escolha in opcoes:
        return opcoes[escolha]
    elif escolha == "4":
        while True:
            valor = input("Digite o tamanho desejado (número): ").strip()
            if valor.isdigit() and int(valor) > 0:
                return int(valor)
            print("Por favor, digite um número válido maior que zero.")
    else:
        print("Opção inválida! Usando 12 caracteres por padrão.\n")
        return 12


def main():
    tamanho = escolher_tamanho()

    while True:
        senha = gerar_senha(tamanho)
        print(f"\nSua senha: {senha}\n")
        print("Pressione [R] para gerar uma nova senha")
        print("Pressione [T] para trocar o tamanho da senha")
        print("Pressione [Q] para sair")

        opcao = input("O que deseja fazer? ").strip().lower()

        if opcao == "r":
            continue  # gera outra senha com o mesmo tamanho
        elif opcao == "t":
            tamanho = escolher_tamanho()
        elif opcao == "q":
            print("\nAté a próxima! 👋")
            break
        else:
            print("\nOpção não reconhecida, gerando nova senha...")


if __name__ == "__main__":
    main()
