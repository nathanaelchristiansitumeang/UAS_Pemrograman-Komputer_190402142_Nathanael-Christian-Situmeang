import socket

listenerSocket = socket.socket()
serverIP = "0.0.0.0"
serverPort = 2222
listenerSocket.bind((serverIP,serverPort))
listenerSocket.listen(0)
while True:
    handlerSocket, addr = listenerSocket.accept()
    print("Client Terkoneksi Dengan Alamat : ", addr)

    pass



