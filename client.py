import socket,threading

class chat_client():
    def __init__(self, username):
        self.s=socket.socket()
        self.username=username
    
    def run(self):
        self.s.connect(("192.168.1.21",4576))
        threading.Thread(target=self.send_messages).start()
        threading.Thread(target=self.listen_server).start()

    def listen_server(self):
        while True:
            data=self.s.recv(2048)
            msg=data.decode("UTF-8")
            print(msg)

    def send_messages(self):
        while True:
            inp=input()
            msg=f"{username}: {inp}"
            self.s.send(msg.encode("UTF-8"))
        
username=input("Nombre de usuario: ")

chat_client(username).run()