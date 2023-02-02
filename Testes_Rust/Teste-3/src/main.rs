extern crate rand;

use std::io;//entrada e saida de dados
use rand::Rng;//tipo de metodo de gerar numeros aleatorio
use std::cmp::Ordering;//confere se um valor è igual(Equal), menor(Less), maior(Greater)

fn main() {

    //let para usar como variavel que pode ser mutavel ou nao
    let val: i32 = rand::thread_rng().gen_range(1..100/* valores de 1 a 100 */);
    //const para criar uma constante que sempre è imutavel
    //const val1: i32 = 31;

    //como seria em C/C++ e rust tb funciona
    //while treu{
    loop {
        
        println!("De um palpite para o numero gerado de 0 a 100:");

        let mut chute = String::new();//aloca variavel do tipo String
    
        //leitura de dados
        io::stdin().read_line(&mut chute)
           .expect("Não foi possível ler");
    
        //redeclarar variavel pode modificar seu valor e tipo
        //converte a variavel chute de String para i32
        let chute = match chute.trim().parse::<i32>(){
            Ok(num) => num,
            Err(_) =>{
                println!("Valor inválido");
                continue;
            },
        };

        //como seria em C/C++ e rust tb funciona
        /*if chute == val{
            println!("valor encontrado era {}", val);
            break
        }else if chute > val{
            println!("Menos");
        }else{
            println!("Mais");
        }*/

        //cmp confere se è igual e retorna um Ordering
        //match decidir o que sera feito com o retorno do cmp
        match chute.cmp(&val){
            Ordering::Less => println!("Mais"),
            Ordering::Greater => println!("Menos"),
            Ordering::Equal => {
                println!("valor encontrado era {}", val);
                break;
            },
        }
    }

    

}
