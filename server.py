import socket

SERVER_IP ="192.168.168.130"
SERVER_PORT = 8080

if __name__ == "__main__":
    #create a socket object. You should know this from CSC 138 CSUS
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #bind the socket with the port
    addr = (SERVER_IP,SERVER_PORT)
    sock.bind(addr)

    #give some ear to the socket
    sock.listen(1)
    
    print("[+] Waiting from incoming connections from ", SERVER_PORT)
    client_sock,client_add = sock.accept()
    print("[+] Succesfuly connected: ", client_add)

    #send a message to the victim machine
    msg = "Hello you have been identified as a victim. With respect your Server"

    client_sock.send(msg.encode())
    #if you open a connection you need to close it
    client_sock.close()
    sock.close()