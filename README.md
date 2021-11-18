# Mini Aplicación

Este repositorio alberga los archivos fuente del mini proyecto de Sistemas Distribuidos, el cual consiste en realizar un servicio de escritura de mensajes usando sockets mediante los protocolos TCP y UDP. Se cuenta con un cliente quien elige a través de una interfaz en consola el tipo de conexión y su nombre de usuario. Por otro lado se tienen dos servidores con funcionalidades similares: Leer el mensaje que envia el cliente, verificar si el usuario esta en la lista de clientes permitido (users.txt), comunicar al usuario si está o no en la lista y guardar un registro(log) en un archivo.

## Detalles técnicos

- Realizado en Python 3.
- Archivos .txt como forma de persistencia de datos.
- Implementación de la libreria sockets de python.
- Manejo de protocolos UDP y TCP.
