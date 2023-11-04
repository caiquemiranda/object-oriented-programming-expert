from random import randint

class Carro:

    def __init__(self, modelo):
        
        self.modelo = modelo
        self.velocidade = 0
        
    def acelerar(self, modelo):
        self.modelo = modelo
        
        if self.modelo == 'sport':
            self.velocidade += randint(10, 30)

        elif self.modelo == 'suv':
            self.velocidade += randint(10, 40)

        elif self.modelo == 'moto':
            self.velocidade += randint(10, 50)

        elif self.modelo == 'truck':
            self.velocidade += randint(10, 20)

        print(f"Acelerando... Velocidade atual: {self.velocidade} km/h")

    def get_velocidade(self):
        return self.velocidade


if __name__ == "__main__":
    
    list_model = ['sport', 'moto', 'truck', 'suv']
    
    print("Digite o modelo do seu Veiculo:")
    print("'sport', 'moto', 'truck', 'suv'") 
    
    modelo = input().lower()
    
    next = True    
    while next:    
        if modelo in list_model:
            meu_carro = Carro(modelo)
            continuar = True
            while continuar:
                print("Escolha uma opção:")
                print("1 - Acelerar")
                print("2 - Ver velocidade atual")
                print("3 - Sair")

                opcao = input()

                if opcao == "1":
                    meu_carro.acelerar(modelo)
                
                    if meu_carro.get_velocidade() >= 100:
                        print("MULTADO! Você ultrapassou a velocidade permitida.")
                        break
                    else:
                        continue
                    
                elif opcao == "2":
                    print(f"Velocidade atual: {meu_carro.get_velocidade()} km/h")
                
                elif opcao == "3":
                    continuar = False
                    modelo = False
                    break
                
                else:
                    print("Opção inválida!")

            print("Fim da aplicação. Até mais!")
            break

        else:
                    print("Opção inválida!")
                    print("Digite o modelo do seu Veiculo:")
                    print("'sport', 'moto', 'truck', 'suv'")
                    modelo = input().lower()
