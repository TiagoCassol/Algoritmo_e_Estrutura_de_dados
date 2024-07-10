# Construa um algoritmo que possua uma tupla com os números escritos
# por extenso de “zero” a “nove”. Peça ao usuário para digitar um número
# de 0 a 9 e retorne a ele o número por extenso, sem usar estruturas
# condicionais (if e switch).

# numExtenso = "zero","um","dois","tres","quatro","cinco","seis","sete","oito","nove"
# escolha = int(input("Escolha uma numero de 0 a 9: "))
# print(numExtenso[escolha])



# Construa um algoritmo que peça ao usuário para informar o nome, a
# nota01 e a nota01 de um aluno. Guarde estas informações em um
# dicionário. Após, calcule a nota final deste aluno [(nota01 + nota02) /2]
# e adicione ao dicionário. Ao final, imprima todos os dados do
# dicionário.

nome = input("Informe seu nome: ")
nota01 = int(input("Informe a nota 1: "))
nota02 = int(input("Informe a nota 2: "))


aluno1 = {
    "nome" : nome,
    "nota 1" : nota01,
    "nota 2" : nota02
}

def somar(nota01, nota02):
    return nota01 + nota02


print(aluno1)
print (somar())


# def somar(x):
#     return x[0] + x[1]
# print(list(map(somar,valores)))

# carro2 = {"modelo": "Doblo", "ano" : 2006}

# print(carro1)
# for chave, valor in carro2.items():
#     print (chave," - ", valor)

# print("-------------------------------")
# for chave in carro1.keys():
#     print(chave, " - ", carro1[chave])

# frota = carro1, carro2 #tupla
# carro3 = {"modelo": "Uno", "ano" : 2004}
# print(frota)
# # frota[1]= carro3
# carro2["modelo"] = "fusca"
# print("---------------------------")
# print(frota)
