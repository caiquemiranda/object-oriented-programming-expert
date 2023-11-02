from random import randint

class Carro:

    def __init__(self, modelo):
        
        self.modelo = modelo
        self.velocidade = 0
        
    def acelerar(self):
        self.velocidade += randint(10, 40)
        print(f"Acelerando... Velocidade atual: {self.velocidade} km/h")

    def get_velocidade(self):
        return self.velocidade


if __name__ == "__main__":
    print("Digite o modelo do seu carro:")
    modelo = input()

    meu_carro = Carro(modelo)

    continuar = True
    while continuar:
        print("Escolha uma opção:")
        print("1 - Acelerar")
        print("2 - Ver velocidade atual")
        print("3 - Sair")

        opcao = input()

        if opcao == "1":
            meu_carro.acelerar()
        
            if meu_carro.get_velocidade() >= 100:
                print("MULTADO! Você ultrapassou a velocidade permitida.")
                break
            else:
                continue
            
        elif opcao == "2":
            print(f"Velocidade atual: {meu_carro.get_velocidade()} km/h")
        
        elif opcao == "3":
            continuar = False
        
        else:
            print("Opção inválida!")

    print("Fim da aplicação. Até mais!")
