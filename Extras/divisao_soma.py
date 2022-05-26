from re import X


num = int(input("Dividendo: "))
num2 = int(input("Divisor: "))
resultado = 0
x = num
while num >= num2:
    num = num - num2
    resultado = resultado + 1
resto = num
print(f"{x} / {num2} = {resultado}  Resto:{resto} ")