import Pyro4

uri = "PYRO:obj_485d4f23cf6545719e6a49a05279e655@localhost:52790"
obj = Pyro4.Proxy(uri)

id = "2"
cidade = "Belo Horizonte"
pais = "Brasil"
nome = "LATAM Airlines"
id_aeroporto = "4"
id_companhia = "2"
horario = "14:00"
aeroporto = "Aeroporto Internacional de Guarulhos"

# Aeroporto
resultado = obj.add_aeroporto(aeroporto, cidade)
# resultado = obj.get_aeroporto()
# resultado = obj.get_aeroporto_id(id)
# resultado = obj.update_aeroporto(id, cidade)
# resultado = obj.delete_aeroporto(id)

# # Companhia Aérea
# resultado = obj.add_companhia(nome, pais)
# resultado = obj.get_companhia()
# resultado = obj.get_companhia_id(id)
# resultado = obj.update_companhia(id, pais)
# resultado = obj.delete_companhia(id)

# # Aeroporto_Companhia
# resultado = obj.add_aeroporto_companhia(id_aeroporto, id_companhia, horario)
# resultado = obj.get_aeroporto_companhia()
# resultado = obj.get_aeroporto_companhia_id(id)
# resultado = obj.update_aeroporto_companhia(id, horario)
# resultado = obj.delete_aeroporto_companhia(id)

print(resultado)
