#!/usr/bin/python
# Create a TCP objet socket and bind it to a port
# Port should be 80, but since it needs root privileges,
# let's use one above 1024
import socket

class Server:
    def parse(self,request):
        """Root of a hierarchy of classes implementing web applications
    This class does almost nothing. Usually, new classes will
    inherit from it, and by redefining "parse" and "process" methods
    will implement the logic of a web application in particular.
    """

        return None

    def process (self , parsedRequest):
        """Parse the received request, extracting the relevant information
        and the HTML page"""

        return (""HTTP/1.1 200 OK", "<html><body><h1>It works!</h1></body></html>")

    def analyze (self , request) :
        numero = peticion.split()[1][1:]
        return numero

    def sum (self , n1 , n2):
        suma = n1 + n2
        return suma


    def __init (self,hostname,port):
        """Initialize the application"""

        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Let the port be reused if no process is actually using it
        mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Bind to the address corresponding to the main name of the host
        mySocket.bind((hostname, port)) #ligar a IP y puerto

        # Queue a maximum of 5 TCP connection requests
        mySocket.listen(5)

        primero = True

        while True:
        print 'Waiting for connections'
        (recvSocket, address) = mySocket.accept()
        print 'Request received:'
        peticion = recvSocket.recv(1234)
        print peticion
        parsedRequest = self.parse(peticion)
        (returnCode,htmlAnswer) = self.process.(parsedRequest)
        numero = self.analyze(peticion)
            if (numero == ''):
                return None
            else :
                    if (primero == True) :
                    resul = int (numero)
                    sumar = 'Otro numero'
                    primero = False

                else :
                    resul = self.sum(resul,int (numero))
                    primero = True
                    suma_total = "La suma es " + str(resul)

                    print ("Answering back :")
                    recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                                            "<html><body>" +
                                            "<p>La suma es :  " +
                                              suma_total +
                                            "</p>" +
                                            "</html></body>" +
                                            "\r\n")

                    recvSocket.close()



"""
 except KeyboardInterrupt:
    print "Closing binded socket"
    mySocket.close()
"""
