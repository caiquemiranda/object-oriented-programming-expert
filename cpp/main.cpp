#include <iostream>

class Carro
{
private:
    std::string modelo;
    int velocidade;

public:
    // Construtor
    Carro(std::string mod) : modelo(mod), velocidade(0) {}

    // Método para acelerar o carro
    void acelerar()
    {
        velocidade += 10;
        std::cout << "Acelerando... Velocidade atual: " << velocidade << " km/h\n";
    }

    // Método para obter a velocidade atual
    int getVelocidade() const
    {
        return velocidade;
    }
};

int main()
{
    std::string modelo;
    std::cout << "Digite o modelo do seu carro: ";
    std::getline(std::cin, modelo);

    Carro meuCarro(modelo);
    int opcao;
    bool continuar = true;

    while (continuar)
    {
        std::cout << "Escolha uma opção:\n";
        std::cout << "1 - Acelerar\n";
        std::cout << "2 - Ver velocidade atual\n";
        std::cout << "3 - Sair\n";
        std::cin >> opcao;

        switch (opcao)
        {
        case 1:
            meuCarro.acelerar();
            break;
        case 2:
            std::cout << "Velocidade atual: " << meuCarro.getVelocidade() << " km/h\n";
            break;
        case 3:
            continuar = false;
            break;
        default:
            std::cout << "Opção inválida!\n";
        }

        // Limpar o buffer de entrada após cada leitura para evitar problemas com std::getline
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    }

    std::cout << "Fim da aplicação. Até mais!\n";

    return 0;
}
