class Sanduiche:
    def tem_carne(self):
        return True
class sanduiche_vegetariano(Sanduiche):
    def tem_carne(self):
        return False

sanduiche = Sanduiche()
print (sanduiche.tem_carne())

sanduichevegetariano = sanduiche_vegetariano()
print (sanduichevegetariano.tem_carne())