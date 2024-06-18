class No:
    def __init__(self, placa, marca, cor):
        self.placa = placa
        self.marca = marca
        self.cor = cor
        self.proximo = None

    def __str__(self):
        return f"Placa: {self.placa}, Marca: {self.marca}, Cor: {self.cor}"
