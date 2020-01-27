from socket import *

servidorPuerto = 12000
servidorSocket = socket(AF_INET,SOCK_STREAM)
servidorSocket.bind(('',servidorPuerto))
servidorSocket.listen(1)
print("El servidor está listo para recibir mensajes")
while 1:
    conexionSocket, clienteDireccion = servidorSocket.accept()
    print("Conexión establecida con ", clienteDireccion)
    mensaje = str( conexionSocket.recv(1024), "utf-8" )
    print("Mensaje recibido de ", clienteDireccion)
    print(mensaje)
    mensajeRespuesta = mensaje

    splitted = mensajeRespuesta.split()

    def isgetfunc(splitted):
        if splitted[0] == 'GET':
            return True

    isget = isgetfunc(splitted)

    if(isget):
        file = open(splitted[1],'r')

    getrespuesta = "HTTP/1.1 200 OK\r\n\r\n"
    print(getrespuesta)
    conexionSocket.send(bytes(getrespuesta, "utf-8"))
    conexionSocket.send(bytes(file.read(), "utf-8"))
    conexionSocket.close()
