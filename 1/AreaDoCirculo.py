import math
import random
print ("--------------Área do circulo---------------")
##raio = int(input("Insira o valor do raio: \n"))
raio = int(random.randint(10, 40))
##randiant int ---- uniform float
area = math.pi* math.pow(raio, 2)
print('Área do circulo: {}, {:.2f}'.format(raio,area))