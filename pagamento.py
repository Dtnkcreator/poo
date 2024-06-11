'''
from datetime import datetime

class Pagamento:
    def __init__(self, vencimento: datetime):
        self.vencimento = vencimento

# Exemplo de uso da classe Pagamento
vencimento = datetime(2024, 6, 30)
pagamento = Pagamento(vencimento)

print(pagamento.vencimento)  # Saída: 2024-06-30 00:00:00
'''

from datetime import datetime

class Pagamento:
    def __init__(self, vencimento: datetime):
        self.vencimento = vencimento

class PagamentoBoleto(Pagamento):
    def __init__(self, vencimento: datetime, codigo_barras: str):
        super().__init__(vencimento)
        self.codigo_barras = codigo_barras

# Exemplo de uso da classe PagamentoBoleto
vencimento = datetime(2024, 6, 30)
codigo_barras = "12345678901234567890"

pagamento_boleto = PagamentoBoleto(vencimento, codigo_barras)

print(f"Vencimento: {pagamento_boleto.vencimento}")
print(f"Código de Barras: {pagamento_boleto.codigo_barras}")
