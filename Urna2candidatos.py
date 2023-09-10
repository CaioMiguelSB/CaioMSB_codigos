ListaDeCandidatos = {22: 'bolsonaro', 13: 'lula'}

i = 1

while i != 0:
    candidato = int(input("selecione o número de seu candidato "))
    if candidato in ListaDeCandidatos:
        nome = ListaDeCandidatos[candidato]
        print(f"Você selecionou o candidato: {nome}")
    break
