import socket 
import hashlib 
import threading 
import json 
import os 

h = hashlib.new("SHA-256") 

def usr_pass(): 

    usrname = input("Username: ")
    passwrd = input("Password: ") 

    return usrname, passwrd 

def verif_user(usrname, passhash):

    with open('user_password.json', 'r') as json_file: 
        data = json.load(json_file) 

    for elem in data: 
        if usrname == elem['usrname'] and passhash == elem['passhash']: 
            return True 
    
    return False 

def send(usrname, usr_socket):
    while True:
        input_message = input("-> ")
        usr_message = usrname + "()" + input_message  
        usr_socket.sendall(usr_message.encode())
        #except usr_socket.error as error:
            #print(os.strerror(error.errno))
    return 

def receive(usr_socket):
    while True: 
        output_message = usr_socket.recv(1024).decode()
        name, msg = output_message.split("()", 1) 
        if usr == "1029321__starter": 
            print(msg)
        else:
            print(f"{usr} : {message}")
    return 
        
def init_user_chatting(usrname):
    host = socket.gethostbyname(socket.gethostname())
    port = 19328
    usr_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #we will have to keep chatting with the server.
    
    usr_socket.connect((host,port))  
    
    #send message to indicate that the user has joined the server room 
    first_message = "1029321__starter()" + usrname + " has joined the party!"
    usr_socket.sendall(first_message.encode())
    
    receiving_thread = threading.Thread(target = send, args = [usrname, usr_socket])

    sending_thread = threading.Thread(target = receive, args = [usr_socket]) 
    
    receiving_thread.start() 

    sending_thread.start()
    #we will have to split this into two different threads, one for sending messages to the server and one for receiving messages from the server


def login_user():    
    
    user_logged = False
    print("Enter your username and password.") 
    
    while user_logged == False: 
        usrname, passwrd = usr_pass()

        h.update(passwrd.encode())
        passhash = h.hexdigest()

        user_logged = verif_user(usrname, passhash)

        if user_logged == False: 
            print("The details you have entered are false.")
            checker = input("Type 'y' if you would like to exit. 'n' if you want to try again.")
            if checker == 'y':
                return
        else: 
            print(f"Welcome, {usrname}!")  
            init_user_chatting(usrname) 
    return 


def create_user():
    
    print("Enter the username and password of the user") 

    usrname, passwrd = usr_pass() 
    
    user_exists = True 

    while user_exists: 
        
        with open('user_password.json', 'r') as json_file: 
            json_values = json.load(json_file)
        
        for elem in json_values: 
            if elem['usrname'] != usrname: 
                user_exists = False
                break
        if len(json_values) == 0: 
            user_exists = False

        if user_exists == True: 
            print("The username already exists, please create a new user with an unique username") 
            usrname, passwrd = usr_pass()

    user_value = [] 

    h.update(passwrd.encode())
    passhash = h.hexdigest() 

    user_value.append({'usrname': usrname, 'passhash': passhash})

    with open('user_password.json', 'a') as json_file:
        json.dump(user_value, json_file, indent = 2, separators=(',',': '))

    print("The user has been created") 
    
    return 


if __name__ == "__main__": 
    
    user_choice = input("Enter 1 to login, 2 to create user, any other option to exit. \n\n") 
    
    if user_choice == '1': 
        login_user() 

    elif user_choice == '2': 
        create_user() 

    else:
        print("User our chatroom again, thank you") 


     
    
