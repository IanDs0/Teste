CREATE DATABASE aeroporto;

USE aeroporto;

CREATE TABLE Aeroporto (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    cidade VARCHAR(50) NOT NULL
);

CREATE TABLE `Companhia Aérea` (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    país VARCHAR(50) NOT NULL
);

CREATE TABLE Aeroporto_Companhia (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_aeroporto INT NOT NULL,
    id_companhia INT NOT NULL,
    horario VARCHAR(5) NOT NULL, -- eu sei que tem a variavel do tipo horário mas deu preguiça de usar
    FOREIGN KEY (id_aeroporto) REFERENCES Aeroporto(id),
    FOREIGN KEY (id_companhia) REFERENCES `Companhia Aérea`(id)
);
