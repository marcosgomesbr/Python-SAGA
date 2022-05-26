tipo_instalação = str(input(
    "Tipo de instalação \n [R] - Residencia \n [I] - Industria \n [C] - Comercial"))
x = tipo_instalação.upper()
# ESSE PROGRAMA TEM ERROS POIS ALGUEM PODE ULTILIZAR O GASTO DE UMA PESSOA RESIDENCIAL MESMO USANDO 5000 khw
# ATUALIZAÇÂO NÂO TEM MAIS
energia = float(input("Quantidade de energia consumida: "))
if x == 'R':

    if energia <= 500:
        print("Seu gasto com energia foi de R$ {}".format(energia * 0.40))
    elif energia >= 501 and energia <= 1000:
        print("Seu gasto com energia foi de R$ {}".format(energia * 0.50))
    else:
        print("Err0r")

elif x == 'I':
    if energia <= 1000:
        print("Seu gasto com energia foi de R$ {}".format(energia * 0.50))
    if energia >= 1001 and energia <= 2500:
        print("Seu gasto com energia foi de R$ {}".format(energia * 0.60))
    else:
        print("VALOR INVVALIDO")

elif x == 'C':
    if energia >= 2500 and energia <=5000:
        print("Seu gasto com energia foi de R$ {}".format(energia * 0.60))
    if energia > 5001:
        print("Seu gasto com energia foi de R$ {}".format(energia * 0.70))
    else:
        print("VALOR INVVALIDO")

else:
    print("INVALIDO")
