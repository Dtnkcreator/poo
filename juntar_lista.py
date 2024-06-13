#exemplo de juntar duas listas e formar uma lista de objeto.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __repr__(self):
        return f" nome = {(self.nome)}, idade = {self.idade} "
    
lista_pessoas = []

list_p = ["Cabral", "Oliveira", "Gama"]
list_n = [30, 35, 40]

for list_p, list_n in zip(list_p, list_n):
    lista_pessoas.append(Pessoa(list_p, list_n))

print(lista_pessoas)