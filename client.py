import socket

handlerSocket = socket.socket()
serverIP = "127.0.0.1"
serverPort = 2222

handlerSocket.connect((serverIP,serverPort))
print("Terkoneksi Dengan Server")
