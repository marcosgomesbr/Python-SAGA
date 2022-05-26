valor_casa = float(input("Valor do imóvel: "))
salario = float(input("Valor so seu salário: "))
quantidade_parcela = float(input("Quantidades de parcelas: "))

valor_parcela = valor_casa/quantidade_parcela

if valor_parcela >= salario*0.30:
    print ("Reprovado")
else:
    print("Aprovado")


