import socket,sys
host=''
port=8080

def middle(mes):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        soc.connect((host, port))
    except:
        print("Connection Error")
        sys.exit()
    soc.send(mes.encode("utf-8"))
    recieve=soc.recv(1024).decode("utf-8")
    return recieve