import random

def escolher_palavra():
    palavras = ["python", "programacao", "git", "github", "colaboracao"]
    return random.choice(palavras)

def exibir_palavra(palavra, letras_adivinhadas):
    return " ".join([letra if letra in letras_adivinhadas else "_" for letra in palavra])

def jogo_da_forca():
    palavra = escolher_palavra()
    letras_adivinhadas = set()
    tentativas = 6

    print("Bem-vindo ao Jogo da Forca!")
    
    while tentativas > 0:
        print("\n" + exibir_palavra(palavra, letras_adivinhadas))
        print(f"Tentativas restantes: {tentativas}")
        tentativa = input("Digite uma letra: ").lower()

        if tentativa in letras_adivinhadas:
            print("Você já tentou essa letra!")
        elif tentativa in palavra:
            print("Boa! Você acertou uma letra!")
            letras_adivinhadas.add(tentativa)
        else:
            print("Ops! Letra errada.")
            tentativas -= 1

        if all(letra in letras_adivinhadas for letra in palavra):
            print(f"\nParabéns! Você adivinhou a palavra: {palavra}")
            break
    else:
        print(f"\nVocê perdeu! A palavra era: {palavra}")

if __name__ == "__main__":
    jogo_da_forca()
