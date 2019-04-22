# client.py
import time, socket, sys

s = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print("Your IPv4: " + ip)
server_ip = input(str("Enter server IPv4: "))
server_port = 50017
s.connect((server_ip, server_port))
s.send("Connected".encode("UTF-8"))
response = s.recv(1024).decode("UTF-8")

while True:
    s.settimeout(60)
    msg = s.recv(1024).decode("UTF-8")
    print(msg)
    message = input(">")
    if message == "close":
        message = "LEFT"
        s.send(message.encode("UTF-8"))
        print("\n")
        break
    s.send(message.encode("UTF-8"))

s.close()