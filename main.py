import sipfullproxy
import socket
import socketserver
import logging
import os
from sys import argv

startPoint = input("Chcete spustit SIP proxy server?[y/n] ")
if startPoint == 'y':
    sipfullproxy.hostname = socket.gethostname()
    sipfullproxy.ipaddress = socket.gethostbyname(sipfullproxy.hostname)
    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (sipfullproxy.ipaddress, sipfullproxy.PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (sipfullproxy.ipaddress, sipfullproxy.PORT)

    logFile = str(os.path.dirname(argv[0])) + '/proxy.log'
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename= logFile, level=logging.INFO, datefmt='%H:%M:%S')

    try:
        with socketserver.UDPServer((sipfullproxy.HOST, sipfullproxy.PORT), sipfullproxy.UDPHandler) as server:
            print("Adresa servera:", sipfullproxy.ipaddress)
            print("Na vypnutie servera stlacte Ctr-C")
            server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        print("Server bol vypnuty")
else:
    print("Server nebol spusteny")
