import numpy as np
X = np.matrix([[0x166B56,0x3050,0x26C7A2,0x247],[0xDD57,0x9D570,0x474,0x1137013],[0x20A9D,0x5A26,0xA5C17,0xDD],[0x91D0,0x1BC,0x1B89B7,0x3417]])
A = np.matrix([[0x2A31C3714,0x518609337,0xC7A0B4C77C5B,0x8159C8CB37B553],[0x7106613281,0x1C893A0A4059,0x2C0386B98181D6,0x87ADD2B5AA56],[0xB656D407,0x8B2765691,0x1915429224DA7,0x242C877009CCB5],[0x21605DD5A,0x5A39D1281,0x99C83296BA8,0x575AAB831044DA]])
Y = X.I * A
key = {Y[0][1], Y[1][0],Y[2][2],Y[3][0]}
print(key)