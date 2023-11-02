using System;

namespace CarroApp
{
    public class Carro
    {
        private string modelo;
        private int velocidade;

        // Construtor
        public Carro(string mod)
        {
            modelo = mod;
            velocidade = 0;
        }

        // Método para acelerar o carro
        public void Acelerar()
        {
            velocidade += 10;
            Console.WriteLine($"Acelerando... Velocidade atual: {velocidade} km/h");
        }

        // Método para obter a velocidade atual
        public int GetVelocidade()
        {
            return velocidade;
        }
    }
}

using System;

namespace CarroApp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Digite o modelo do seu carro:");
            string modelo = Console.ReadLine();

            Carro meuCarro = new Carro(modelo);

            bool continuar = true;
            while (continuar)
            {
                Console.WriteLine("Escolha uma opção:");
                Console.WriteLine("1 - Acelerar");
                Console.WriteLine("2 - Ver velocidade atual");
                Console.WriteLine("3 - Sair");

                int opcao;
                if (int.TryParse(Console.ReadLine(), out opcao))
                {
                    switch (opcao)
                    {
                        case 1:
                            meuCarro.Acelerar();
                            break;
                        case 2:
                            Console.WriteLine($"Velocidade atual: {meuCarro.GetVelocidade()} km/h");
                            break;
                        case 3:
                            continuar = false;
                            break;
                        default:
                            Console.WriteLine("Opção inválida!");
                            break;
                    }
                }
                else
                {
                    Console.WriteLine("Por favor, insira um número válido.");
                }
            }

            Console.WriteLine("Fim da aplicação. Até mais!");
        }
    }
}

