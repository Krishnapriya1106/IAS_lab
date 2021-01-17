import socket
import sys
import traceback
from threading import Thread
import os
import mimetypes
def main():
   start_server()
def start_server():
   host = "127.0.0.1"
   port = 8000
   soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   print("Socket created")
   try:
      soc.bind((host, port))
   except:
      print("Bind failed. Error : " + str(sys.exc_info()))
      sys.exit()
   soc.listen(10)
   print("Socket now listening")
   while True:
      connection, address = soc.accept()
      ip, port = str(address[0]), str(address[1])
      print("Connected with " + ip + ":" + port)
      try:
        Thread(target=clientThread, args=(connection,ip,port)).start()
      except:
        print("Thread did not start.")
        traceback.print_exc()
   soc.close()
  
    
def clientThread(connection, ip, port, max_buffer_size = 5120):
   client_input = connection.recv(max_buffer_size)
   client_input_size = sys.getsizeof(client_input)
   decoded_input = client_input.decode("utf8").rstrip()
   if(decoded_input.find("HTTP")==-1):
      path=decoded_input[4:]
      try:
         size=os.path.getsize(path)
         connection.send(bytes(str(size).encode("utf8")))
         cont=open(path,'rb')
         buffer=cont.read(1024)
         while buffer:
            connection.send(buffer)
            buffer=cont.read(1024)
      except:
         print("FILE NOT PRESENT")
         connection.close()
         sys.exit()
   else:
       x=decoded_input.find("HTTP")
       file=decoded_input[5:x-1]
       try:
         msg=open(file,"rb").read()
         content=mimetypes.guess_type(file)[0] or 'text/html'
         response="HTTP/1.1 200 OK\r\nContent-Type:"+content+"\r\nContent-Disposition:attachment;filename="+file+"\r\n\r\n"
         connection.send(response.encode('UTF-8')+msg)
       except:
         response="HTTP/1.1 404 Page not Found\r\nContent-Type:text/html\r\n\r\n"+"<html><body><h1>File Not Present in the server!!!!</h1></body</html>"
         connection.send(response.encode())
         sys.exit()
         connection.close()
       
  
if __name__ == "__main__":
   main()