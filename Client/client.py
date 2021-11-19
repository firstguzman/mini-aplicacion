import socket

HOST = 'localhost'
PORT = 19876

def conversation_tcp (sock):
    try:
        name = input('Introduce el nombre de usuario: ')
        # Send data
        header = 'helloiam '
        message = header + name
        print('sending {!r}'.format(message))
        sock.sendall(message.encode('utf-8'))
        data = sock.recv(2048)

        print('received {!r}'.format(data))

        if data == b'OK':
            response = input('Escriba su mensaje: ')
            message = 'f '+ response
            sock.sendall(message.encode('utf-8'))
            print('response sent')

    finally:
        print('closing socket')
        sock.close()

def conversation_udp (sock, server_address):
    try:
        name = input('Introduce el nombre de usuario: ')
        # Send data
        header = 'helloiam '
        message = header + name
        print('sending {!r}'.format(message))
        sock.sendto(message.encode('utf-8'), server_address)
        data = sock.recvfrom(4096)

        print('received {!r}'.format(data))

        if data[0] == b'OK':
            response = input('Escriba su mensaje: ')
            message = 'f '+ response
            sock.sendto(message.encode('utf-8'), server_address)
            print('response sent')

    finally:
        print('closing socket')
        sock.close()


while True:
    print("""
    1. TCP
    2. UDP

    0. Salir
    """)

    ans = input('Seleccione el protocolo: ')
    if ans == '1':
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = (HOST, PORT)
        print('connecting to {} port {}'.format(*server_address))
        sock.connect(server_address)

        conversation_tcp(sock) 

    elif ans == '2':
        # Create a UDP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Connect the socket to the port where the server is listening
        server_address = (HOST, PORT)
        print('connecting to {} port {}'.format(*server_address))
        sock.connect(server_address)


        conversation_udp(sock, server_address) 

        print('\n Opcion no disponible')
    elif ans == '0':
        break
    else:
        print("\n Seleccione una opción válida")
