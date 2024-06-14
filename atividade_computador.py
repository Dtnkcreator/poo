class Computador:


    def __init__(self, cpu_p, qntd_memoria_p, ligado_p):
        self.cpu = cpu_p
        self.qntd_memoria = qntd_memoria_p
        self.ligado = ligado_p

    def ligar(self):

        self.ligado = True
        print("O computador ligou! (COMPUTADOR LIGADO)" )

    def desligar(self):

        self.ligado = False
        print("O computador desligou! (COMPUTADOR DESLIGADO)")

class Pc_Gamer(Computador):
    def __init__(self, cpu_p, qntd_memoria_p, ligado_p, jogando_p):
        super().__init__(cpu_p, qntd_memoria_p, ligado_p)
        self.jogando = jogando_p
    def iniciar_jogo(self):
    
        self.jogando = True
        print("Você está jogando! (PC GAMER JOGANDO)")

    def fechar_jogo(self):

        self.jogando = False
        print("Você parou de jogar! (PC GAMER PAROU DE JOGAR)")

pc1= Computador("i5", "8GB", False)
gamer1 = Pc_Gamer("i7", "64GB", False, False)


gamer1.iniciar_jogo()
pc1.ligar()
pc1.desligar()

print(f"COMPUTADOR - CPU: {pc1.cpu} MEMÓRIA: {pc1.qntd_memoria} LIGADO: {pc1.ligado}")
print(f"PC GAMER - CPU: {gamer1.cpu} MEMÓRIA: {gamer1.qntd_memoria} LIGADO: {gamer1.ligado}, JOGANDO: {gamer1.jogando}")