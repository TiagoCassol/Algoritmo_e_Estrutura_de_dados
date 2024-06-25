from Livro import Livro
from Pilha import Pilha

l1 = Livro("Harry potter", "JK rowling",67)
l2 = Livro("O Cortiço", "Aluiso de Azevedo",65)
l3 = Livro("Feliz Ano Velho", "Marcelo Rubens Paiva",97)
l4 = Livro("Hamlet", "William Shakespeare ",87)

pilha = Pilha()
pilha.imprimir()

pilha.add(l1)
pilha.add(l2)
pilha.add(l3)
pilha.remover()
pilha.add(l4)
pilha.remover()
pilha.remover()
pilha.remover()
pilha.remover()
