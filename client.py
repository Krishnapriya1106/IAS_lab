import socket
import sys
def main():
   soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   host = "127.0.0.1"
   port = 8000
   message = input()
   print(message)
   try:
      soc.connect((host, port))
   except:
      print("Connection Error")
      sys.exit()
   if message[0:3]=="GET":
      soc.send(message.encode("utf8"))
      x=message.rfind("/")
      if x==-1:
         s=message[4:]
      else:
         s=message[x+1:]
      f=open(s,'wb')
      recieved=soc.recv(1024).decode("utf8")
      if not recieved:
         sys.exit()
      r=int(recieved)
      while r>0:
         recieved=soc.recv(1024)
         f.write(recieved)
         r=r-1024
      f.close()
if __name__ == "__main__":
   main()