import socket
N=object
n=str
z=socket.AF_INET
d=socket.SOCK_STREAM
import random
import math
class J(object):
 @classmethod
 def P(cls, n):
  return cls(n)
 def __init__(self, n):
  self.n = n
  self.n_sq = n * n
  self.g = n+1
 def __repr__(self):
  return "<PublicKey: %s>" % self.n

N=8610097151964530250458416477078839753866992124382816129264561552780058479042617122846698948133143173906596827136174737789262313134794392619210115458939713
M=J(N)
l=(2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97) # 1 ~ 100 prime

def T(a, b, n):
 A = a = long(a % n)
 yield A
 t = 1L
 while t <= b:
  t <<= 1
 t >>= 2
 while t:
  A = pow(A, 2, n)
  if t & b:
   A = (A * a) % n
  yield A
  t >>= 1

def H(bits):
 return max(40, 2 * bits)

def V(u, L):
 return 1 not in T(u, L-1, L)

def D(L, k=None):
 if L == 1:
  return True
 if k is None:
  k = H(L.bit_length())
 for i in l:
  if L == i:
   return True
  if L % i == 0:
   return False
 for i in xrange(k):
  u = random.randrange(2, L-1) | 1
  if V(u, L):
   return False
 return True

def b(bits, k=None):
 assert bits>=8
 if k is None:
  k = H(bits)
 while True:
  L = random.randrange(2**(bits-1)+1,2**bits) | 1
  if D(L, k):
   return L

def i(M, plain):
 while True:
  r = b(long(round(math.log(M.n, 2))))
  if r > 0 and r < M.n:
   break
 x = pow(r, M.n, M.n_sq)
 t = (pow(M.g, plain, M.n_sq) * x) % M.n_sq
 return t


try:
 W = socket.socket(z, d)
 W.connect(("210.65.10.132",15678))
 W.recv(1024)
 cy = 29801527264134575869358824949363537946953189756457143465541710188744075519958765829338135560408361427814191704817283839012277050755161434979281387129105782467121091212685245293690128389771604410687201656050020228327135789333958688763687456978648149928416224937059831306490593367854224834009680601552938219969L
 W.send(str(cy))
 I = W.recv(1024)
 print I
finally:
 W.close()

