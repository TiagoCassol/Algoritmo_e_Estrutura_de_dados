from Cidade import Cidade

class Pessoa:

    def __init__(self, nome, idade = 18,cid = Cidade("porto")):
        self.id = None
        self.nome = nome
        self.idade = idade
        self.cidade = cid

    def __str__(self):
        texto = "Nome: "+ self.nome
        texto += "\nIdade:" + str(self.idade)
        return texto