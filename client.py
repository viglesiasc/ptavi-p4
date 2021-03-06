#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket
import sys

try:
    # Constantes. Dirección IP del servidor y contenido a enviar
    SERVER = sys.argv[1]
    PORT = int(sys.argv[2])
    SIP_DIRECTION = sys.argv[4]
    EXPIRES = sys.argv[5]
except:
    sys.exit('Usage: client.py ip puerto register sip_address expires_value')

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, PORT))
    LINE_ = ("REGISTER " + 'sip:' + SIP_DIRECTION + ' SIP/2.0\\r\\n\\r\\n\n')
    LINE = (LINE_ + 'Expires: ' + str(EXPIRES) + '\\r\\n\\r\\n')
    print('\n')
    print(LINE)
    my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))

print("Socket terminado.")
print('\n')
