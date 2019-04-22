# server.py
import time, socket, sys

s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 50017
s.bind((ip, port))
print("Your IPv4: " + ip)
           
s.listen(1)
conn, addr = s.accept()

msg = conn.recv(1024).decode("UTF-8")

conn.send(msg.encode())

while True:
    msg = input(str(">"))
    if msg == "close":
        msg = "LEFT"
        conn.send(msg.encode("UTF-8"))
        print("\n")
        break
    conn.send(msg.encode("UTF-8"))
    conn.settimeout(60)
    msg = conn.recv(1024).decode("UTF-8")
    print(msg)

conn.close()