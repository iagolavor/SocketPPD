#Criar um INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind the socket to a public host, and a well-known port
serversocket.bind((socket.gethostname(), 80))
#virar um socket servidor
serversocket.listen(5)

while True:
    #aceitar conexões de fora
    (clientsocket, address) = serversocket.accept()
    #fazer algo com o socket cliente
    #nesse caso vamos fingir que é um servidor com threads
    ct = client_thread(clientsocket)
    ct.run()