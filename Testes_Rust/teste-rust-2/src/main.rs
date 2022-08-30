use std::io;

struct nome {
    nome: String,
    idade: i32,//int
    vivo: bool,
    peso: f32,//float
    notas: [i32;10],//array

}

//não é bom fazer assim mas por agora vai servir
fn scanf(ler: &mut String) {
    io::stdin()
        .read_line(ler)
        .expect("Erro de leitura");
}
fn main() {
    let mut ler = String::new();
    scanf(&mut ler);
    println!("{}",ler);
}

