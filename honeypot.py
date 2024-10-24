import socket
import datetime

# Configuraciones
HOST = '0.0.0.0'  # Escuchar en todas las interfaces
PORT = 9999  # Puerto a escuchar

# Crear socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Honeypot escuchando en {HOST}:{PORT}...")

while True:
    try:
        client_socket, addr = server_socket.accept()
        print(f"Conexión desde {addr}")

        # Guardar información sobre la conexión
        with open('honeypot_log.txt', 'a') as log_file:
            log_file.write(f"{datetime.datetime.now()} - Conexión desde {addr}\n")
        
        # Enviar respuesta (opcional)
        client_socket.send(b"Hola, has alcanzado un honeypot!\n")
        
        # Cerrar la conexión
        client_socket.close()
    except KeyboardInterrupt:
        print("Deteniendo el honeypot...")
        server_socket.close()
        break
