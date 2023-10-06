import socket

HEADER = 64
PORT = 5060
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECTED"
SERVER = socket.gethostbyname(socket.gethostname())
NICKNAME = "NICK:"
ADDR = (SERVER, PORT)


NICKNAME = str(input("First, set your nickname: "))



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

print(f"Connected with: {ADDR}")
print("Feel free to send message or leave by using /leave command")


def send_msg(msg):

    message = msg.encode(FORMAT)
    msg_lengt = len(message)
    send_lenght = str(msg_lengt).encode(FORMAT)
    send_lenght += b' ' * (HEADER - len(send_lenght))
    client.send(send_lenght)
    client.send(message)

send_msg(NICKNAME)
connection = True

while connection:
    msg = str(input(f"{NICKNAME}: "))

    if msg == '/leave':
        
        send_msg(DISCONNECT_MSG)
        break
    else: 

        send_msg(msg)