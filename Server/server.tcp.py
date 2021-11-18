import socket
from datetime import datetime

def findByname (nombre):
    with open('users.txt', encoding='utf-8') as file:
        users = file.readlines()
    for user in users:
        if nombre in user:
            return True
    return False

def saveLog (filename, message, date, ip, protocol):
    with open(filename, 'ab') as log_file:
        log_message = message + '. Recibido a las: ' + date + ' y enviado por: ' + ip + ' a través del protocolo ' +  protocol + '\n'
        log_message_utf = log_message.encode()
        log_file.write(log_message_utf)



HOST = 'localhost'
PORT = 19876

# Create a TCP/IP socket
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = (HOST, PORT)
print('starting up on {} port {}'.format(*server_address))
socket_server.bind(server_address)

# Listen for incoming connections
socket_server.listen()

while True:
    # Wait for a connection
    print('Waiting for a connection')
    connection, client_address = socket_server.accept()
    try:
        print(f'Connection from {client_address} has been established!')
        session = True
        while session:
            data = connection.recv(2048)
            if not data:
                break

            data_transformed = data.decode('utf-8')
            
            if 'helloiam' in data_transformed:
                name = data_transformed.replace('helloiam ', '')
                if findByname(name):
                    connection.sendall(bytes('OK', 'utf-8'))
                else: 
                    error_message = 'Usuario inexistente'
                    connection.sendall(bytes(error_message, 'utf-8'))
                    print('saving log...')
                    today = datetime.today()
                    saveLog('log.txt', error_message, today.strftime("%d/%m/%Y %H:%M:%S"), client_address[0], 'TCP')
                    session = False

            if 'Hola soy' in data_transformed:
                print('saving log...')
                today = datetime.today()
                saveLog('log.txt', data_transformed, today.strftime("%d/%m/%Y %H:%M:%S"), client_address[0], 'TCP')
                break
    finally:
        # Clean up the connection
        connection.close()