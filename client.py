import socket

# Below 4 line are necessary to start client.
s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host,port))

inp = "Connection started"
while inp!="exit":          # when you type 'exit' connection will ends
    inp = input(">> ")      # waiting for data to send to server
    sInput = inp.encode()   # encode string to byte
    s.send(sInput)          # sending to remote server

s.close()
