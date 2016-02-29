#!/usr/bin/python
# Create a TCP objet socket and bind it to a port
# Port should be 80, but since it needs root privileges,
# let's use one above 1024
import socket


mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Let the port be reused if no process is actually using it
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind to the address corresponding to the main name of the host
mySocket.bind(('localhost', 1234)) #ligar a IP y puerto

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)
primero = 'none'
try:
    while True:
        print 'Waiting for connections'
        (recvSocket, address) = mySocket.accept()
        print 'Request received:'
        peticion = recvSocket.recv(1234)
        try :
            print 'La peticion es : ' + peticion
            numero = peticion.split()[1][1:]
            print 'El numero a sumar es ' + numero
            num = int(numero)
        except ValueError:
                print 'Pon un numero para continuar'
                print ("Answering back :")
                recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                            "<html><body>ERROR: Necesitas poner un numero para continuar </body></html>" +
                            "\r\n")
                continue

        if primero == 'none':
            primero = num
            prim = int(primero)
            print ("Answering back :")
            recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                                    "<html><body> Recibido el primer sumando</body></html>" +
                                    "\r\n")

        else :
            ans = num + prim
            print ("Answering back :")
            recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                                    "<html><body>" +
                                    "<p>La suma es :  " +
                                     str(num) + "+" + str(prim) + "=" + str(ans) +
                                    "</p>" +
                                    "</html></body>" +
                                    "\r\n")
            print ans
        #primero = 'none'

        recvSocket.close()

except KeyboardInterrupt:
    print "Closing binded socket"
    mySocket.close()
