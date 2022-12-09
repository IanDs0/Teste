import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('127.0.0.1', 5000))
server.listen(1)

connection, address = server.accept()

namefile = connection.recv(1024).decode()

arquivo = open (namefile, "rb")
ler_buffer = arquivo.read(1024) 
while (ler_buffer):
    connection.send(ler_buffer) 
    ler_buffer = arquivo.read(1024)
print ("OK")
while True:
    print("\t")