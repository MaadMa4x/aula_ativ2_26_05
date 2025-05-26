class Aluno:
    def __init__(self, nome, matrícula, curso):
        self.nome = nome
        self.matrícula = matrícula
        self.curso = curso 


p1 = Aluno("Maria", "776", "NEM")
p2 = Aluno("João", "786", "TDS")


print(p1.nome, p1.matrícula, p1.curso)  
print(p2.nome, p2.matrícula, p1.curso)  
