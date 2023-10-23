print("Em qual situação você se encontra?")
print("""1: Gestante;
2: Idoso;
3: Cadeirante;
4: Nenhuma das anteriores.""")
situacao = int(input("Eu me enquadro na situação n° "))
if (situacao == 1) or (situacao == 2) or (situacao == 3) :
    print("""Você é cliente prioritário.
    Por favor, vá até a fila preferencial.""")
else :
    print("""Você não é cliente prioritário.
    Por favor, vá até a fila comum.""")


