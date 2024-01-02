line_idade = input("Digite sua idade:")
idade = int(line_idade)
# código da linha 2 (definir que o numero que vai ser colocar é inteiro.)

if idade >= 60:
    print("Você é um idoso")
# código da linha 5 e 6 é para quando o numero for igual ou maior que 60 (print linha 5).

elif idade >= 18:
    print("Você é maior de idade, adulto")
# código da linha 9 e 10 é para quando o numero for igual ou maior que 18 (print linha 10).

else:
    print("Você é menor de idade")