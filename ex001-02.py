Na1 = int(input ("Digite um número: "))
Nb2 = int(input ("Digite um número: "))
Nc3 = int(input ("Digite um número: "))

soma = Na1 + Nb2

if Na1 + Nb2 == Nc3:
    print(f"O valor da soma {Na1} + {Nb2} = {soma} é igual ao item 3 -> {Nc3}")

elif Na1 + Nb2 < Nc3:
    print(f"o valor da soma {Na1} + {Nb2} = {soma} é menor que o item 3 -> {Nc3}")

else:
    print(f"o valor da soma {Na1} + {Nb2} = {soma} é maior que o item 3 -> {Nc3}")