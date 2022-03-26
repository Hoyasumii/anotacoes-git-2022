print("Calculadora")
n1 = int(input("Digite aqui o seu primeiro número: "))
n2 = int(input("Digite aqui o seu segundo número: "))

op = ["+", "-", "*", "/"]

while True:
    print("Escolha a operação:")

    for i in range(len(op)):
        print(f"\t[{i + 1}] {op[i]}")

    aop = int(input("Digite aqui a sua resposta: "))
    
    if aop > 0 and aop <= len(op):
        print(eval(f"O Resultado da Operação é: {n1}{op[aop - 1]}{n2}"))
        break