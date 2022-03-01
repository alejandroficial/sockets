import socket,threading

class chat():
    def __init__(self):
        self.s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connections=[]

    def listen_client(self,conn,addr):
        while True:
            data=conn.recv(2048)
            print(data.decode("UTF-8"))

    def send_to_clients(self,msg):
        for conn in self.connections:
            conn.send(msg)

    def run(self):
        self.s.bind(("192.168.1.21",4576))
        self.s.listen(5)
        while True:
            conn,addr=self.s.accept()
            self.connections.append(conn)
            threading.Thread(target=self.listen_client,args=(conn,addr,)).start()

chat().run()