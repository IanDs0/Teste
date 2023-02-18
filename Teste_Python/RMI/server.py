import Pyro4
import mysql.connector

@Pyro4.expose
class MeuObjetoRemoto:

    # Cria uma conexão com o banco de dados
    cnx = mysql.connector.connect(
        user='ian',
        password='7543',
        host='localhost',
        database='aeroporto'
    )

    # Aeroporto
    def add_aeroporto(self, nome, cidade):
        # Cria um cursor para executar comandos SQL
        cursor = self.cnx.cursor()

        query = "INSERT INTO `aeroporto`.`aeroporto` (`nome`, `cidade`) VALUES ('" + nome + "', '" + cidade + "');"
        cursor.execute(query)
        self.cnx.commit()

        # Fecha o cursor
        cursor.close()
        return "Adcionado o Aeroporto"

    def get_aeroporto(self):
        # Cria um cursor para executar comandos SQL
        cursor = self.cnx.cursor()

        query = "SELECT * FROM `aeroporto`;"
        cursor.execute(query)

        # Armazena os resultados da consulta
        results = cursor.fetchall()

        # Fecha o cursor
        cursor.close()
        return results

    def get_aeroporto_id(self, id):
        # Cria um cursor para executar comandos SQL
        cursor = self.cnx.cursor()

        query = "SELECT * FROM `aeroporto` WHERE id = " + id + ";"
        cursor.execute(query)

        # Armazena os resultados da consulta
        results = cursor.fetchall()

        # Fecha o cursor
        cursor.close()
        return results

    def update_aeroporto(self, id, cidade):
        # Cria um cursor para executar comandos SQL
        cursor = self.cnx.cursor()

        query = "UPDATE Aeroporto SET cidade = '" + cidade +"' WHERE id = " + id + ";"
        cursor.execute(query)
        self.cnx.commit()

        # Fecha o cursor
        cursor.close()
        return "Update o Aeroporto"

    def delete_aeroporto(self, id):
        # Cria um cursor para executar comandos SQL
        cursor = self.cnx.cursor()

        query = "DELETE FROM Aeroporto WHERE id = " + id + ";"
        cursor.execute(query)
        self.cnx.commit()

        # Fecha o cursor
        cursor.close()
        return "Delete o Aeroporto"



    # Companhia Aérea
    def add_companhia(self, nome, pais):
        # Cria um cursor para executar comandos SQL
        cursor = self.cnx.cursor()

        query = "INSERT INTO `Companhia Aérea` (nome, país) VALUES ('"+nome+"', '"+pais+"');"
        cursor.execute(query)
        self.cnx.commit()

        # Fecha o cursor
        cursor.close()
        return "Adcionado o Companhia Aérea"

    def get_companhia(self):
        # Cria um cursor para executar comandos SQL
        cursor = self.cnx.cursor()

        query = "SELECT * FROM `companhia aérea`;"
        cursor.execute(query)

        # Armazena os resultados da consulta
        results = cursor.fetchall()

        # Fecha o cursor
        cursor.close()
        return results

    def get_companhia_id(self, id):
        # Cria um cursor para executar comandos SQL
        cursor = self.cnx.cursor()

        query = "SELECT * FROM `companhia aérea` WHERE id = " + id + ";"
        cursor.execute(query)

        # Armazena os resultados da consulta
        results = cursor.fetchall()

        # Fecha o cursor
        cursor.close()
        return results

    def update_companhia(self, id, pais):
        # Cria um cursor para executar comandos SQL
        cursor = self.cnx.cursor()

        query = "UPDATE `companhia aérea` SET país = '" + pais + "' WHERE id = " + id + ";"
        cursor.execute(query)
        self.cnx.commit()

        # Fecha o cursor
        cursor.close()
        return "Update o Companhia Aérea"

    def delete_companhia(self, id):
        # Cria um cursor para executar comandos SQL
        cursor = self.cnx.cursor()

        query = "DELETE FROM `companhia aérea` WHERE id = " + id + ";"
        cursor.execute(query)
        self.cnx.commit()

        # Fecha o cursor
        cursor.close()
        return "Delete o Companhia Aérea"



    # Aeroporto_Companhia
    def add_aeroporto_companhia(self, id_aeroporto, id_companhia, horario):
        # Cria um cursor para executar comandos SQL
        cursor = self.cnx.cursor()

        query = "INSERT INTO Aeroporto_Companhia (id_aeroporto, id_companhia, horario) VALUES ("+id_aeroporto+", "+id_companhia+", '"+horario+"');"
        cursor.execute(query)
        self.cnx.commit()

        
        return "Adcionado o Voo"

    def get_aeroporto_companhia(self):
        # Cria um cursor para executar comandos SQL
        cursor = self.cnx.cursor()

        query = "SELECT * FROM `Aeroporto_Companhia` ;"
        cursor.execute(query)

        # Armazena os resultados da consulta
        results = cursor.fetchall()

        # Fecha o cursor
        cursor.close()
        return results

    def get_aeroporto_companhia_id(self, id):
        # Cria um cursor para executar comandos SQL
        cursor = self.cnx.cursor()

        query = "SELECT * FROM `Aeroporto_Companhia` WHERE id = " + id + ";"
        cursor.execute(query)

        # Armazena os resultados da consulta
        results = cursor.fetchall()

        # Fecha o cursor
        cursor.close()
        return results

    def update_aeroporto_companhia(self, id, horario):
        # Cria um cursor para executar comandos SQL
        cursor = self.cnx.cursor()

        query = "UPDATE Aeroporto_Companhia SET horario = '"+horario+"' WHERE id = "+id+";"
        cursor.execute(query)
        self.cnx.commit()

        
        return "Update o Voo"

    def delete_aeroporto_companhia(self, id):
        # Cria um cursor para executar comandos SQL
        cursor = self.cnx.cursor()

        query = "DELETE FROM `Aeroporto_Companhia` WHERE id = " + id + ";"
        cursor.execute(query)
        self.cnx.commit()

        # Fecha o cursor
        cursor.close()
        return "Delete o Voo"

daemon = Pyro4.Daemon()
uri = daemon.register(MeuObjetoRemoto)

print("URI do objeto remoto:", uri)

daemon.requestLoop()
