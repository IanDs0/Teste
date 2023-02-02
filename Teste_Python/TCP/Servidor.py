import socket
import threading

class Server:
    def __init__(self, host='localhost', port=8000):
        self.host = host
        self.port = port
        self.clients = []

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()

    def broadcast(self, message):
        for client in self.clients:
            client.send(message)

    def receive(self, client):
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                self.broadcast(message.encode('utf-8'))
            except:
                index = self.clients.index(client)
                self.clients.pop(index)
                client.close()
                break

    def accept(self):
        print("Server running on {}:{}".format(self.host, self.port))
        while True:
            client, address = self.server.accept()
            print("Connected to {}".format(str(address)))
            client.send("".encode('utf-8'))
            self.clients.append(client)
            client_thread = threading.Thread(target=self.receive, args=(client,))
            client_thread.start()

server = Server()
server.accept()
