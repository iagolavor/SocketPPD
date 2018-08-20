import socket
import threading
from queue import Queue

"""s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)

server = 'pythonprogramming.net'
port = 80
server_ip = socket.gethostbyname(server)
print(server_ip)

request = "GET / HTTP/1.1\nHost: "+server+"\n\n"
s.connect((server, port))
s.send(request.encode())
result = s.recv(4096) #Quantidade de memoria(BUFFER) que vc vai usar para baixar coisas
#print(result)

while(len(result)>0):
    print(result)
    result = s.recv(4096)"""

#escanear quais portas estao abertas, pode fazer um for com port para saber qual
"""def pscan(port):
    try:
        s.connect((server, port))
        return True
    except:
        return False"""

#Parte de thread do tutorial

"""print_lock = threading.Lock()

target = 'pythonprogramming.net'
def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target, port))
        with print_lock:
            print('port',port,'is open!')
        con.close
    except:
        pass

def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()

q = Queue()

for x in range(100):
    t = threading.Thread(target = threader)
    t.daemon = True
    t.start()

for worker in range(1,10000):
    q.put(worker)

q.join()"""

"""#Binding and listening with sockets
import sys
host = ''
port = 7070
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((host,port))
except socket.error as e:
    print(str(e))

s.listen(5)

con, addr = s.accept()
print('connected to '+addr[0]+': '+str(addr[1])) """
#Sistema de cliente-servidor com socket

