package main

import "fmt"

type Carro struct {
	modelo    string
	velocidade int
}

func (c *Carro) Acelerar() {
	c.velocidade += 10
	fmt.Printf("Acelerando... Velocidade atual: %d km/h\n", c.velocidade)
}

func (c *Carro) GetVelocidade() int {
	return c.velocidade
}


package main

import (
	"fmt"
	"os"
)

func main() {
	var modelo string
	fmt.Println("Digite o modelo do seu carro:")
	fmt.Scanln(&modelo)

	meuCarro := Carro{modelo: modelo}

	for {
		fmt.Println("Escolha uma opção:")
		fmt.Println("1 - Acelerar")
		fmt.Println("2 - Ver velocidade atual")
		fmt.Println("3 - Sair")

		var opcao int
		fmt.Scanln(&opcao)

		switch opcao {
		case 1:
			meuCarro.Acelerar()
		case 2:
			fmt.Printf("Velocidade atual: %d km/h\n", meuCarro.GetVelocidade())
		case 3:
			fmt.Println("Fim da aplicação. Até mais!")
			os.Exit(0)
		default:
			fmt.Println("Opção inválida!")
		}
	}
}
