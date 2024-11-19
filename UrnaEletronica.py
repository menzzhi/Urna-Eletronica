print("-------------------------------------------------------------------------")
print("- Bem-vindo a sua Urna Eletrônica!                                      -")
print("- Abaixo, será descrito o número de cada candidato e o respectivo nome. -")
print("-------------------------------------------------------------------------")

print(" ")

print("1 - Gabriel")
print("2 - Laura")
print("3 - Guilherme")
print("4 - Leandro")
print(" ")
print("5 - NULO")
print("6 - BRANCO")
print("0 - SAIR URNA")
print("ATENÇÃO! Qualquer número digitado além desses informados, serão DESCONSIDERADOS.")

print(" ")

numeroTotalDeVotos = 0
candidatoGabriel = 0
candidatoLaura = 0
candidatoGuilherme = 0
candidatoLeandro = 0
votoNulo = 0
votoBranco = 0

while True:
    print("Para sair da urna, digite '0' ")
    numeroDigitado = int(input("Digite o número escolhido: "))
    print(" ")

    print("Votando...")

    print(" ")

    print("Voto confirmado!")

    print(" ")

    if numeroDigitado == 1:
        candidatoGabriel = candidatoGabriel + 1
        numeroTotalDeVotos = numeroTotalDeVotos + 1
        # print(candidatoGabriel)
        # print(numeroTotalDeVotos)
    elif numeroDigitado == 2:
        candidatoLaura = candidatoLaura + 1
        numeroTotalDeVotos = numeroTotalDeVotos + 1
        # print(candidatoLaura)
        # print(numeroTotalDeVotos)
    elif numeroDigitado == 3:
        candidatoGuilherme = candidatoGuilherme + 1
        numeroTotalDeVotos = numeroTotalDeVotos + 1
        # print(candidatoGuilherme)
        # print(numeroTotalDeVotos)
    elif numeroDigitado == 4:
        candidatoLeandro = candidatoLeandro + 1
        numeroTotalDeVotos = numeroTotalDeVotos + 1
        # print(candidatoLeandro)
        # print(numeroTotalDeVotos)
    elif numeroDigitado == 5:
        votoNulo = votoNulo + 1
        numeroTotalDeVotos = numeroTotalDeVotos + 1
        # print(votoNulo)
        # print(numeroTotalDeVotos)
    elif numeroDigitado == 6:
        votoBranco = votoBranco + 1
        numeroTotalDeVotos = numeroTotalDeVotos + 1
        # print(votoBranco)
        # print(numeroTotalDeVotos)
    elif not numeroDigitado != 0:
        break

print("O Total de votos que cada candidato recebeu foi: ")
print("Gabriel: ", candidatoGabriel)
print("Laura: ", candidatoLaura)
print("Guilherme: ", candidatoGuilherme)
print("Leandro: ", candidatoLeandro)
print("Nulo: ", votoNulo)
print("Branco: ", votoBranco)