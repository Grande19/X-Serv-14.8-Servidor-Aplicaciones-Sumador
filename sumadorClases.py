#!/usr/bin/python
# Create a TCP objet socket and bind it to a port
# Port should be 80, but since it needs root privileges,
# let's use one above 1024
#pasado a pyton 3 mediante el comado 2to3

import socket

class webApp:
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

        return ("HTTP/1.1 200 OK" , "<html><body><h1>It works!</h1></body></html>")

    def __init__(self, hostname, port):
        """Initialize the web application."""

        # Create a TCP objet socket and bind it to a port
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        mySocket.bind((hostname, port))

        # Queue a maximum of 5 TCP connection requests
        mySocket.listen(5)

        # Accept connections, read incoming data, and call
        # parse and process methods (in a loop)

        while True:
            print ('Waiting for connections')
            (recvSocket, address) = mySocket.accept()
            print ('HTTP request received (going to parse and process):')
            request = recvSocket.recv(2048)
            print (request)
            parsedRequest = self.parse(request)
            (returnCode, htmlAnswer) = self.process(parsedRequest)
            print ('Answering back...')
            recvSocket.send(str.encode("HTTP/1.1 " + returnCode + " \r\n\r\n"
                            + htmlAnswer + "\r\n"))
            recvSocket.close()

"""

    def __init (self,hostname,port):
        Initialize the application

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

class sumApp(webApp): #heredo de webApp
        """Clase para sumar"""


        def parse(self , request):
            try:
                numero  = int(request.split()[1][1:])
                valido = True
            except ValueError:
                """Me va a saltar el favicon.ico que es una petición
                para mostrar el icono que sale en el navegador """
                numero = 0
                valido = False
            return numero,valido

        def process (self ,parsedRequest ) :
            numero,valido = parsedRequest #parsedRequest es una tupla
            if not valido :
                return ("HTTP/1.1 200 OK" , "<html><body><h1>Dame numeros</h1></body></html>")
            if self.primero:
                self.guardado = numero #para que quede guaradado el "guardado"
                self.primero = False
                return ("HTTP/1.1 200 OK" , "<html><body><h1>Dame otro numero</h1></body></html>")

            else :
                resultado = self.guardado + numero
                self.primero = True
                return ("HTTP/1.1 200 OK" , "<html><body><h1>Resultado : " + str(resultado) + "</h1></body></html>")

        def __init__ (self , hostname , port):
            self.primero = True
            """Ejecuta primero el init del padre"""
            super(sumApp ,self).__init__(hostname,port) #python3
            #webApp.__init__(hostname , port )

if __name__ == "__main__" :
    testWebApp = sumApp ("localhost" , 1234)
