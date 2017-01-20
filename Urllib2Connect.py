import urllib2

def Connect(name):
    
    
    response = urllib2.urlopen(name)
    
    
    
    print "Reply:\n",response.read()
    
    response.close()
    
name = "http://dangbo.hcmute.edu.vn/"
Connect(name)
