carros = "Uno","Doblo","Renegade","Hilux"
print(carros)
print(carros[2])
print(carros[1:3])
print(carros[1:-1])
print(carros[2:])

#ERRO
# carros[1]="fucas" n podemos mudar as tuplas, a tupla é imutavel
def calcular(x,y):
    return x + y, x-y, x*y,x / y

print(calcular(10,5))

a,b,c,d = calcular(9,3)
print("Soma: ", a)
print("Subtração: ", b)
print("Multiplicador ", c)
print("Divisão: ", d)

resultados = calcular(15,5)
for x in resultados:
    print(x)