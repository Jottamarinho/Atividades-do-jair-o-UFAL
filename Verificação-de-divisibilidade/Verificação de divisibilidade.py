def verifica_divisibilidade(numero, divisor):
    return numero % divisor == 0


numberone = int(input("Digite o primeiro número: "))
numbertwo = int(input("Digite o segundo número: "))


if verifica_divisibilidade(numberone, numbertwo):
    print(f"{numberone} é divisível por {numbertwo}")
else:
    print(f"{numberone} não é divisível por {numbertwo}")
