from pwn import *

def back(banum):
    return banum * 123

def drawfunction(drnum):
    banum = (drnum + 60) * 10
    return back(banum)

def setpar(senum):
    drnum = senum / 20
    return drawfunction(drnum)

def getparameter(parameter):
    number = parameter * 100
    ganum = number * 10 + 500
    hanum = ganum / 2 + 70
    senum = hanum * 20 + 80 * parameter
    return str(setpar(senum))

conn = remote("210.65.10.170", 9487)

conn.recvuntil("parameter = ")
n = int(conn.recv())
print(n)
conn.sendline(getparameter(n))
print(conn.recv())

