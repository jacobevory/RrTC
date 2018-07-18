import socket


TCP_IP = '192.168.1.80'
TCP_PORT = 20250
BUFFER_SIZE = 1024
MESSAGE = "<washSoft><addTail><id>592484</id><washPkgNum>16</washPkgNum></addTail></washSoft>"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE.encode('utf-8'))
data = s.recv(BUFFER_SIZE)
s.close()
print ("received data:", data)