from Categoria import Categoria
from Desktop import Desktop
from Notebook import Notebook

categoria1 = Categoria(1, "Eletrônicos")
    
desktop1 = Desktop("HP", "preto", 3000.00, categoria1, "500W")
print(desktop1.getInformacoes())
desktop1.cadastrar()
    
notebook1 = Notebook("Dell", "branvo", 2500.00, categoria1, "8 horas")
print(notebook1.getInformacoes())
notebook1.cadastrar()