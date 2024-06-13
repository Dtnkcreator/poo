class Car:

    def __init__(self, nome_p, marca_p, preco_p, ano_p, cor_p):
        self.nome = nome_p
        self.marca = marca_p
        self.preco = preco_p
        self.ano = ano_p
        self.cor = cor_p

car1 = Car("Fiat Uno", "Fiat", 50990, 2020, "branco")

print(f"{car1.nome}, {car1.marca}, R${car1.preco}, {car1.ano}, {car1.cor}")