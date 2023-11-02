pub struct Carro {
    modelo: String,
    velocidade: i32,
}

impl Carro {
    pub fn new(modelo: &str) -> Carro {
        Carro {
            modelo: modelo.to_string(),
            velocidade: 0,
        }
    }

    pub fn acelerar(&mut self) {
        self.velocidade += 10;
        println!("Acelerando... Velocidade atual: {} km/h", self.velocidade);
    }

    pub fn get_velocidade(&self) -> i32 {
        self.velocidade
    }
}

use std::io;

fn main() {
    println!("Digite o modelo do seu carro:");
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let modelo = input.trim();

    let mut meu_carro = Carro::new(modelo);

    loop {
        println!("Escolha uma opção:");
        println!("1 - Acelerar");
        println!("2 - Ver velocidade atual");
        println!("3 - Sair");

        input.clear();
        io::stdin().read_line(&mut input).unwrap();
        let opcao = input.trim();

        match opcao {
            "1" => meu_carro.acelerar(),
            "2" => println!("Velocidade atual: {} km/h", meu_carro.get_velocidade()),
            "3" => break,
            _ => println!("Opção inválida!"),
        }
    }

    println!("Fim da aplicação. Até mais!");
}
