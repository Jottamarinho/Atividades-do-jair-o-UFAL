numberone = float(input("Digite o primeiro numero:"))
numbertwo = float(input("Digite o segundo numero:"))

numberone = int(numberone)
numbertwo = int(numbertwo)

resultado = numberone % numbertwo == 0

if resultado == 0:
    print("O primeiro numero é divisivel pelo segundo")
    resultado = numberone / numbertwo
    print("resultado da divisão:", resultado)
else:
    print("O primeiro numero não é divisivel pelo segundo")
