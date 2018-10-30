#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys

PORT = int(sys.argv[1])
dic = {}


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        """
        handle method of the server class
        (all requests will be handled by this method)
        """
        print('\n')
        text = self.rfile.read()
        client_text = text.decode('utf-8').split(' ')

        direction_sip = client_text[1][4:]
        print("IP cliente: ", self.client_address[0])
        print("Puerto cliente: ", self.client_address[1])
        dic[direction_sip] = self.client_address[0]
        expires_time = int(client_text[3][:-10])
        # print(expires_time)
        if expires_time == 0:
            del dic[direction_sip]
        if len(dic) == 0:
            print('Without SIP directions')
        else:
            print(dic)

        print('\n')
        self.wfile.write(b"SIP/2.0 200 OK\\r\\n\\r\\n")

if __name__ == "__main__":
    # Listens at localhost ('') port 6001
    # and calls the EchoHandler class to manage the request
    serv = socketserver.UDPServer(('', PORT), SIPRegisterHandler)

    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
        # self.wfile.write(b"SIP/2.0 200 OK\\r\\n\\r\\n")
    except KeyboardInterrupt:
        print("Finalizado servidor")
