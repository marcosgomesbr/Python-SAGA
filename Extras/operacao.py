print("Escolha a Operação \n [1]-Soma \n [2]-Subtração \n [3]-Multiplicação \n [4]-Divisão ")
mat = int(input("Digite: "))
op = 0
if mat == 1:
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))
    op = num1 + num2
    print(op)
elif mat == 2: 
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))
    op = num1 - num2
    print(op)
elif mat == 3: 
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))
    op= num1 * num2
    print(op)
elif mat == 4: 
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))
    op = num1 / num2
    print(op)
else:
    print("Número INVALIDO")