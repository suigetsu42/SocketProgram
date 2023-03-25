import socket
import threading 


HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())                         #Gets the IPv4 address
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECTED -_-"




server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                  #Specifies address we are looking for i.e IPv4
server.bind(ADDR)                                                           #Binds address to server 

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg_length == DISCONNECT_MESSAGE:
                connected = False
            
            print(f"[{addr}] {msg}")
            conn.send("Yaaaay!!!!! I love CSCI-434-02W because the course instructor is really awesome : - )".encode(FORMAT))
            
    
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")                        #Tells us the number of threads running - 1

                
print("[STARTING] server is starting...")
start()