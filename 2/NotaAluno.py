nota1 =  float(input("Informe a primeira nota do aluno: "))
nota2 =  float(input("Informe a segunda do aluno: "))
media =  (nota1 + nota2) / 2
print (media)
if media >= 9 and media <= 10:
    print("Conceito do Aluno: S")
elif media >= 7.5 and media <= 9:
    print("Conceito do Aluno: A")

elif media >= 6 and media <= 7.5:
    print("Conceito do Aluno: B") 

elif media >= 5 and media <= 6:
    print("Conceito do Aluno: C")    
else:
    print("Reprovado")