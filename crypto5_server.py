import socket
h=pow
j=True
i=socket.socket
k=socket.AF_INET
V=socket.SOCK_STREAM
import threading
import random
J=random.getrandbits
import hashlib
import binascii
import Crypto.Cipher.AES
p="Bob"
P=0xEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3D
l="0xEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3D"
G=2
B="2"
def Y(O,E):
 try:
  v=O.recv(1024).rstrip("\n").split("||")
  ga=int(v[1])
  b=random.getrandbits(80)
  gb=pow(G,b,P)
  t="Hi, I'm Bob||{0}".format(gb)
  O.send(t)
  k=pow(ga,b,P)
  Q=hashlib.pbkdf2_hmac('md5',pow(ga,b,P),b'5566',100000)
  b=O.recv(1024).rstrip("\n")
  A=Crypto.Cipher.AES.new(Q)
  a=A.decrypt(b)
  if a==AUTH:
   n=A.encrypt(FLAG)
   O.send(n)
  else:
   O.send("Wrong answer! Try again!")
 finally:
  O.close()
def x():
 try:
  s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  s.bind(("210.65.10.132",35566))
  s.listen(10)
  while True:
   O,E=s.accept()
   T=threading.Thread(target=Y,args=(O,E))
   T.start()
 finally:
  s.close()

if __name__=="__main__":
 x()
