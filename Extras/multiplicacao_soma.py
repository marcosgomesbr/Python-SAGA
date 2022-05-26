num = int(input("Multiplicado: "))
num2 = int(input("Multiplicador: "))
x = 1
y = 0
while x <= num2:
    y = y + num
    x = x + 1
    print(f"{num} X {num2} = {y}")