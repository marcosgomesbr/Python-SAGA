t = int(input("Tabuada de : "))
inicio = int(input("Inicio da tabuada: "))
fim = int(input("Fim da tabuada: "))
while inicio <= fim:
    print(f"{t} x {inicio} = {t*inicio}")
    inicio += 1