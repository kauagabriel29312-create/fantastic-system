import subprocess


def test_mensagem_com_nome():
    # Simula o usuário digitando "Kauã"
    resultado = subprocess.run(
        ["python", "ola_devops.py"],
        input="Kauã\n",       # envia o texto "Kauã" como se fosse digitado
        capture_output=True,
        text=True
    )
    assert "Olá, Kauã! Bem-vindo ao DevOps." in resultado.stdout


def test_mensagem_sem_nome():
    # Simula o usuário apenas apertando Enter (nome vazio)
    resultado = subprocess.run(
        ["python", "ola_devops.py"],
        input="\n",           # apenas Enter
        capture_output=True,
        text=True
    )
    assert "Olá, Visitante! Bem-vindo ao DevOps." in resultado.stdout
