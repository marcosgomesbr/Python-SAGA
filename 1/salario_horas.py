horas = int(input("Valor por hora: "))
horasTrabalhadas = int(input("Horas trabalhadas: "))
valorFinal = horasTrabalhadas*horas
imposto =  valorFinal*11/100
inss = valorFinal*8/100    
sind = valorFinal*5/100
print('Desconto: R$ {}'.format(imposto + inss + sind))
print('Salario Bruto: R$ R$ {}'.format(valorFinal))
print('Salario Liquido: R$ {}'.format(valorFinal - imposto - inss - sind))