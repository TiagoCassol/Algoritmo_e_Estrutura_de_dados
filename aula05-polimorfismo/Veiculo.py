from Categoria import Categoria

class Veiculo:

    def __init__(self, marca="Fiat" , ano = 2014,cat = Categoria("SUV")):
        self.id = None
        self.marca = marca
        self.ano = ano
        self.categoria = cat

    def __str__(self):
        texto = "\nVeiculo: \nmarca: "+ self.marca + "\nAno: "+ str(self.ano) + "\nCategoria: "+self.categoria.nome
        return texto

    def imprimir(self):
        print(self)