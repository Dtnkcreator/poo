class Animal:
    def __init__(self, nome: str, idade: int, cor: str, raca: str):
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.raca = raca

class Peixe(Animal):
    def __init__(self, nome: str, idade: int, cor: str, raca: str, habitat_natural: str):
        super().__init__(nome,idade, cor, raca)
        self.habitat_natural = habitat_natural
# Exemplo de uso da classe Animal e Cachorro
animal = Animal(nome="Rex", idade=5, cor = "Marrom", raca="Labrador")
print(f"Animal: {animal.nome}, Idade: {animal.idade}, Cor do Pelo: {animal.cor}, Raça: {animal.raca}")

peixe1 = Peixe(nome="Nemo", idade = 1, cor="Laranja, preto e branco", raca = "peixe palhaço", habitat_natural="oceano")
print(f"Peixe: {peixe1.nome}, Idade: {peixe1.idade}, Cor: {peixe1.cor}, Raça: {peixe1.raca}, Habitat: {peixe1.habitat_natural}")

