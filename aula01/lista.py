
nomes_produtos = ["Arroz", "Feijão", "Macarrão"]
precos_produtos = [10.5, 5.99, 3.75]
quantidades_produtos = [20, 15, 30]

def imprimir_produto(indice):
    if indice < len(nomes_produtos):
        nome = nomes_produtos[indice]
        preco = precos_produtos[indice]
        quantidade = quantidades_produtos[indice]
        print(f"Produto: {nome}, Preço: R${preco}, Quantidade: {quantidade}")
    else:
        print("Índice inválido.")

def retirar_produto():
    indice = int(input("Digite o número do item que deseja excluir: "))
    if indice >= 0 and indice < len(nomes_produtos):
        del nomes_produtos[indice]
        del precos_produtos[indice]
        del quantidades_produtos[indice]
        print("Produto removido com sucesso.")
    else:
        print("Índice inválido.")

print("Lista de produtos:")
for i in range(len(nomes_produtos)):
    imprimir_produto(i)

print("\nRemovendo um produto:")
retirar_produto()

print("\nLista de produtos atualizada:")
for i in range(len(nomes_produtos)):
    imprimir_produto(i)
