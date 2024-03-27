class Aluno:

    def __init__(self, nome, matricula):
        self.id = None
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        texto = "Nome: "+ self.nome
        texto += "\nmatricula:" + str(self.matricula)
        return texto

    def imprimir(self):
        print(self.nome,self.matricula)

class AlunoEnsinoMedio(Aluno):
    def __init__(self,nome, matricula, ano):
        Aluno.__init__(self,nome, matricula)
        self.ano = ano
        
    def imprimir(self):
        print(self.nome,self.matricula,self.ano)
.
class AlunoGraduacao(Aluno):
    def __init__(self,nome,matricula,semestre):
        Aluno.__init__(self,nome,matricula)
        self.semestre = semestre
    
    def imprimir(self):
        print(self.nome,self.matricula,self.semestre)