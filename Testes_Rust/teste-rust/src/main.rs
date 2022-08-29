extern crate ferris_says;

use ferris_says::say;
use std::io;
use std::io::{ stdout, BufWriter };

fn main() {
    
    let mut hello ="Hello word RUST! ".to_string();
    let mut ler = String::new();
    let width = 24;//imutavel
    //let mut tam = 20;//mutatvel

    //saida de dados
    let mut writer = BufWriter::new(stdout());
    
    //scanf feito
    io::stdin()
        .read_line(&mut ler)
        .expect("Erro de leitura");

    //concaterna starg
    hello.push_str(&ler);
    let out = hello.as_bytes();

    say(out,width, &mut writer).unwrap();
    
}