class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __repr__(self):
        return f"< nome = {(self.nome)}, idade = {self.idade} >"
    
pessoa1 = Pessoa("Clara", 16)
pessoa2 = Pessoa("Evaldo", 23)
pessoa3 = Pessoa("Sérgio", 46)

lista_pessoas = [pessoa1, pessoa2, pessoa3]

for pessoa in lista_pessoas:
    print(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}")

#print(lista_pessoas)