import socket,server_system,sys

def stub():
    host=''
    port=8080
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        soc.bind((host, port))
    except:
        print("Bind failed. Error : " + str(sys.exc_info()))
        sys.exit()
    while True:
        soc.listen(1)
        connection, address = soc.accept()
        ip, port = str(address[0]), str(address[1])
        string=connection.recv(1024).decode("utf-8")
        list1=string.split()
        length=len(list1)
        expr='server_system.'+list1[0]+'('
        for i in range(1,length-1):
            expr=expr+'"'+list1[i]+'",'
        expr=expr+'"'+list1[length-1]+'")'
        try:
            func=eval(expr)
            connection.send(str(func).encode("utf-8"))
            connection.close()
        except:
            connection.send("No such function on server side".encode("utf-8"))
            connection.close()

if __name__=="__main__":
    stub()