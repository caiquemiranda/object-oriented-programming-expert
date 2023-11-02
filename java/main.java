public class Carro {
    
    // Atributos
    private String modelo;
    private int velocidade;
    
    // Construtor
    public Carro(String modelo) {
        this.modelo = modelo;
        this.velocidade = 0;
    }
    
    // Método para acelerar o carro
    public void acelerar() {
        velocidade += 10;
        System.out.println("Acelerando... Velocidade atual: " + velocidade + " km/h");
    }

    // Método para obter a velocidade atual
    public int getVelocidade() {
        return velocidade;
    }

    // Outros métodos getters e setters (omitidos por brevidade)
}


import java.util.Scanner;

public class AplicacaoCarro {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Digite o modelo do seu carro:");
        String modelo = scanner.nextLine();
        
        Carro meuCarro = new Carro(modelo);
        
        boolean continuar = true;
        while (continuar) {
            System.out.println("Escolha uma opção:");
            System.out.println("1 - Acelerar");
            System.out.println("2 - Ver velocidade atual");
            System.out.println("3 - Sair");
            
            int opcao = scanner.nextInt();
            
            switch (opcao) {
                case 1:
                    meuCarro.acelerar();
                    break;
                case 2:
                    System.out.println("Velocidade atual: " + meuCarro.getVelocidade() + " km/h");
                    break;
                case 3:
                    continuar = false;
                    break;
                default:
                    System.out.println("Opção inválida!");
            }
        }
        
        System.out.println("Fim da aplicação. Até mais!");
    }
}
