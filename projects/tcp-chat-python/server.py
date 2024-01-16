import socket 
import threading 
import time 


#lock = threading.Lock()

# requirements 


# creation of server socket and other requirements 

def welcome_server(): 
    print("Welcome to the Enkav chatting space.\n")
    print("Other users will join you as you keep speaking. \n")
    
    return 

def start_server():
    host = socket.gethostbyname(socket.gethostname())
    port = 19328
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen() 
    
    while True: 
        conn, addr = server_socket.accept()
        
        new_user_thread = threading.Thread(target = create_new_thread, args = [server_socket, conn, addr])
        new_user_thread.start() 
    return 

def create_new_thread(server_socket, conn, addr):
    print("True")
    while True: 
        request = conn.recv(1024)
        #server_socket.sendall(request)
        output_message = request.decode()
        
        usr, msg = output_message.split("()", 1) 
        if usr == "1029321__starter":
            print(msg) 
        else: 
            print(f"{usr} : {msg}")
    return 


# handling multiple clients 


if __name__ == "__main__": 

    welcome_server()

    start_server()
