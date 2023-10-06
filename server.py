import socket
import threading

HEADER = 64
PORT = 5060
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECTED"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

client_nicknames = {}

def handle_client(conn, addr):

    print(f"New connection from : {addr}")
    connected = True
    nickname = None
    while connected:

        msg_lenght = conn.recv(HEADER).decode(FORMAT)

        if msg_lenght:

            msg_lenght = int(msg_lenght)
            msg = conn.recv(msg_lenght).decode(FORMAT)

            if nickname is None:
                nickname = msg
                client_nicknames[conn] = nickname

            elif msg == DISCONNECT_MSG:
                connected = False
                print(f"{nickname}: Disconnected" )

            else:
                print(f"{nickname}: {msg}")
                
    if conn in client_nicknames:
        del client_nicknames[conn]
    conn.close()

def start_server():
    
    print(f"Server is listening on: {SERVER}")
    server.listen()

    while True:
        conn, addr= server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread. start()
        
        print(f"Active connections: {threading.active_count()-1}")

start_server()