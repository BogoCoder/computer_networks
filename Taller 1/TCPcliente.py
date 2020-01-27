from socket import *

servidorNombre = "127.0.0.1"
servidorPuerto = 12000
clienteSocket = socket(AF_INET, SOCK_STREAM)
clienteSocket.connect((servidorNombre,servidorPuerto))
mensaje = "GET ./decla HTTP/1.1\r\n"
clienteSocket.send(bytes(mensaje, "utf-8"))
mensajeRespuesta = clienteSocket.recv(1024)
print("Respuesta:\n" + str(mensajeRespuesta, "utf-8"))
clienteSocket.close()
