
#Torre:id, nome, endereco | cadastrar():void,imprimir():void

class Torre:

    def __init__(self, nome, endereco ):
        self.nome = nome
        self.endereco = endereco

    def __str__(self):
        return self.nome + " - " + self.endereco 

    def imprimir(self):
            print("--------Torres-------")
            if self.inicio == None:
                    print("Nenhuma torre registrada")
            else:
                    print("lista de torres")
                    aux = self.inicio
                    texto = ""
                    while aux:
                        texto += aux.dado + " - "
                        aux = aux.proximo
                    print(texto)