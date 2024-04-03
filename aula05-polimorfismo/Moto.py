from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self,marca,ano,cat,cilindradas):
        super().__init__(marca,ano,cat)
        self.cilindradas = cilindradas

    def __str__(self):
        texto = "\nMoto: \nmarca: "+ self.marca + "\nAno: "+ str(self.ano) + "\nCategoria: "+self.categoria.nome+ "\nCilindradas: "+str(self.cilindradas)
        return texto

