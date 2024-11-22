import time
import os

print("-------------------------------------------------------------------------")
print("- Bem-vindo a sua Urna Eletrônica!                                      -")
print("- Vote utilizando o painel abaixo: ")
print("-------------------------------------------------------------------------")

time.sleep(4)

print(" ")

print("1 - Gabriel")
print("2 - Laura")
print("3 - Guilherme")
print("4 - Leandro")
print(" ")
print("5 - NULO")
print("6 - BRANCO")
print(" ")
print("0 - *SAIR DA URNA*")
print(" ")

time.sleep(4)

numeroTotalDeVotos = 0
candidatoGabriel = 0
candidatoLaura = 0
candidatoGuilherme = 0
candidatoLeandro = 0
votoNulo = 0
votoBranco = 0

while True:

    numeroDigitado = int(input("Digite o número escolhido: "))

    print(" ")

    if numeroDigitado == 0: break

    print("Votando...")

    time.sleep(3)

    print(" ")

    print("Voto confirmado!")

    print(" ")

    time.sleep(1)

    match numeroDigitado:
        case 1:
            candidatoGabriel = candidatoGabriel + 1
            numeroTotalDeVotos = numeroTotalDeVotos + 1
        case 2:
            candidatoLaura = candidatoLaura + 1
            numeroTotalDeVotos = numeroTotalDeVotos + 1
        case 3:
            candidatoGuilherme = candidatoGuilherme + 1
            numeroTotalDeVotos = numeroTotalDeVotos + 1
        case 4:
            candidatoLeandro = candidatoLeandro + 1
            numeroTotalDeVotos = numeroTotalDeVotos + 1
        case 5:
            votoNulo = votoNulo + 1
            numeroTotalDeVotos = numeroTotalDeVotos + 1
        case 6:
            votoBranco = votoBranco + 1
            numeroTotalDeVotos = numeroTotalDeVotos + 1

    # votarNovamente = str(input("Deseja votar novamente? S/N: "))

    # print(" ")

    # if votarNovamente != 'S' and votarNovamente != 's': break

print("O Total de votos foi de:",numeroTotalDeVotos,". E o voto que cada candidato recebeu foi: ")
print(" ")
print("Gabriel: ", candidatoGabriel)
print("Laura: ", candidatoLaura)
print("Guilherme: ", candidatoGuilherme)
print("Leandro: ", candidatoLeandro)
print("Nulo: ", votoNulo)
print("Branco: ", votoBranco)

print(" ")

porcentagemDeVotosNulos = (votoNulo / numeroTotalDeVotos) * 100
porcentagemNuloFormatado = "{:.2f}".format(porcentagemDeVotosNulos)

porcentagemDeVotosBrancos = (votoBranco / numeroTotalDeVotos) * 100
porcentagemBrancoFormatado = "{:.2f}".format(porcentagemDeVotosBrancos)
print("Houve %", porcentagemNuloFormatado ,"de votos nulos e %", porcentagemBrancoFormatado ,"de votos brancos sobre o total de votos. ")

print(" ")

if candidatoGabriel > candidatoLaura and candidatoGabriel > candidatoGuilherme and candidatoGabriel > candidatoLeandro :
    print("O candidato Gabriel ganhou as eleições!")
elif candidatoLaura > candidatoGabriel and candidatoLaura > candidatoGuilherme and candidatoLaura > candidatoLeandro :
    print("A candidata Laura ganhou as eleições!")
elif candidatoGuilherme > candidatoGabriel and candidatoGuilherme > candidatoLaura and candidatoGuilherme > candidatoLeandro :
    print("O candidato Guilherme ganhou as eleições!")
elif candidatoLeandro > candidatoGabriel and candidatoLeandro > candidatoLaura and candidatoLeandro > candidatoGuilherme :
    print("O candidato Leandro ganhou as eleições!")