def mensagem(nome):
    print(f"Olá, {nome}! Bem-vindo ao DevOps.")


if __name__ == "__main__":
    nome_usuario = input("Digite seu nome: ").strip()
    if not nome_usuario:
        nome_usuario = "Visitante"
    mensagem(nome_usuario)

# <-- linha em branco aqui