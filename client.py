import socket

username=input("Nombre de usuario: ")

with socket.socket() as s:
    s.connect(("192.168.1.21",4576))
    while True:
        inp=input("> ")
        msg=f"{username}: {inp}"
        s.send(msg.encode("UTF-8"))