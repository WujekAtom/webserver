import socket

# Below 5 lines are necessary to start server
s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host,port))
s.listen(5)


c, addr = s.accept()    # accepting connection from remote client
while True:
    data = c.recv(1024) # receive data from remote client
    if not data: break  # if no connection from remote then do not wait for data
    print(data)         # echo what client send
    #c.send(data)
c.close()

