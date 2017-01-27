import socket
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#gan socket bang cong 8081
server_address = ("AnHo", 8081)
print "Starting up on %s port %s" % server_address
server.bind(server_address)

# Nghe ngong dong tinh tu clien 
# cung cap mot hang so la so nguoi cua queue neu co nhieu lk cung luc
server.listen(5)

# Cho ket noi
connection, client_address = server.accept()
print "Connection from:", connection.getpeername()

# Nhan request tu client
data = connection.recv(4096)
if data:
    print"Received!", repr(data)
    
    # Tra loi mot cach ro rang
    data = data.rstrip()
    connection.send("%s\n%s\n%s\n" % ('-'*80, bytearray(data.center(80)), '-'*80))
    print"Respond sent!"    

# Ngat ket noi
connection.shutdown(socket.SHUT_RD | socket.SHUT.WR)
connection.close()
print "Connection closed"

# Ngung nhan request, ngung nghe ngon tu client luon
server.close()
