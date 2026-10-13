import socket

s = socket.socket()
s.connect(("127.0.0.1", 8000))
s.send(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
print(s.recv(2000).decode())
s.close()