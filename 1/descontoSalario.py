horas = float(input("Valor por hora: "))
horasTrabalhadas = float(input("Horas trabalhadas: "))
bruto = horasTrabalhadas*horas
inss = bruto*0.08
impostoRenda = bruto*0.11
sindicato = bruto*0.05

print('Salario bruto: R${}'.format(bruto))
print('Desconto INSS: R${}'.format(bruto-inss))
print('Desconto IR: R${}'.format(bruto-impostoRenda))
print('Desconto sindicato: R${}'.format(bruto-sindicato))
print('Salario Liquido: R${}'.format(bruto-inss-impostoRenda-sindicato))
