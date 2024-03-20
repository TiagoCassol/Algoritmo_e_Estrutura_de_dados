def calcular_area_retangulo(altura, largura):
    area = altura * largura
    return area

altura = float(input("Digite a altura do retângulo: "))
largura = float(input("Digite a largura do retângulo: "))

area = calcular_area_retangulo(altura, largura)
print("A área do retângulo é:", area)

print("Por favor, insira valores numéricos para altura e largura.")
