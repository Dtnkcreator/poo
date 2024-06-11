'''
class Aluno:
    def __init__(self, idade):
        self.idade = idade

    def verifica_idade(self):
        if self.idade > 18:
            print("O aluno é maior de idade.")
        else:
            print("O aluno é menor de idade.")

# Exemplo de uso da classe Aluno
aluno1 = Aluno(20)
aluno1.verifica_idade()  # Saída: O aluno é maior de idade.

aluno2 = Aluno(16)
aluno2.verifica_idade()  # Saída: O aluno é menor de idade.
'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def verifica_nome_idade(self):
        print(f"O nome da pessoa é {self.nome} e a sua idade é de {self.idade} anos.")

pessoa1 = Pessoa("Juca", 40)
pessoa1.verifica_nome_idade()

pessoa2 = Pessoa("Nathan", 24)
pessoa2.verifica_nome_idade()