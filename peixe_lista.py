'''
Lista_peixe = []

class Peixe:
    def __init__(self, especie_p, tipo_de_agua_p, profundidade_encontrada_p):
        self.especie = especie_p
        self.tipo_de_agua = tipo_de_agua_p
        self.profundidade_encontrada = profundidade_encontrada_p

    def __repr__(self):
        return f" Espécie = {(self.especie)}, Tipo de Água = {self.tipo_de_agua}, Profundidade Encontrada: {self.profundidade_encontrada} " 

nomes_peixe = ["Linguado", "Salmão", "Pirarucu", "Peixe-palhaço", "Peixe Lua"]
tipo_agua = ["Salgada", "Salgada", "Doce", "Salgada", "Salgada"]
profundidade = ["100m", "200m", "200m", "13m", "70m"]

for nomes_peixe, tipo_agua, profundidade in zip(nomes_peixe, tipo_agua, profundidade):
    Lista_peixe.append(Peixe(nomes_peixe, tipo_agua, profundidade))

print(Lista_peixe)

'''

class Peixe:
    def __init__(self, especie_p, tipo_de_agua_p, profundidade_encontrada_p):
        self.especie = especie_p
        self.tipo_de_agua = tipo_de_agua_p
        self.profundidade_encontrada = profundidade_encontrada_p

    def __repr__(self):
        return f" Espécie = {(self.especie)}, Tipo de Água = {self.tipo_de_agua}, Profundidade Encontrada: {self.profundidade_encontrada} " 

peixe1 = Peixe("Linguado", "Salgada", "100m")
peixe2 = Peixe("Salmão", "Salgada", "200m")
peixe3 = Peixe("Pirarucu", "Doce", "200m")
peixe4 = Peixe("Peixe-palhaço", "Salgada", "13m")
peixe5 = Peixe("Peixe Lua", "Salgada", "70m")

lista_peixe = [peixe1, peixe2, peixe3, peixe4, peixe5]

print(lista_peixe)