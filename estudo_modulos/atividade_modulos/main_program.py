import soma
import subtracao
import multiplicacao
import divisao

def Operacoes():
    try:
        pergunta = int(input("Qual operação deseja realizar? 1. Adição 2. Subtração 3. Multiplicação 4. Divisão   "))

        match pergunta:
            case 1:
                numero_1 = int(input("Digite o primeiro número:  "))
                numero_2 = int(input("Digite o segundo número:  "))
                soma_acao = soma.Adicao(numero_1, numero_2)
                soma_acao.somar()
            case 2:
                numero_1 = int(input("Digite o primeiro número:  "))
                numero_2 = int(input("Digite o segundo número:  "))
                subtracao_acao = subtracao.Subtracao_1(numero_1, numero_2)
                subtracao_acao.subtrair()
            case 3:
                numero_1 = int(input("Digite o primeiro número:  "))
                numero_2 = int(input("Digite o segundo número:  "))
                multiplicacao_acao = multiplicacao.Multiplicao(numero_1, numero_2)
                multiplicacao_acao.multiplicar()
            case 4:
                numero_1 = int(input("Digite o primeiro número:  "))
                numero_2 = int(input("Digite o segundo número:  "))
                divisao_acao = divisao.Divisao(numero_1, numero_2)
                divisao_acao.dividir()
            case _:
                print ("A opção escolhida não está disponível, tente novamente.")
                Operacoes()
        
    except:
        print("Ocorreu um erro, tente novamente.")
        Operacoes()

Operacoes()