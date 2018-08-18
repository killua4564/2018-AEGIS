from pwn import *

conn = remote("210.71.253.105", 8080)

text2morse = {"0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..", ".": ".-.-.-", ",": "--..--", "?": "..--..", "!": "-.-.--", "-": "-....-", "/": "-..-.", "@": ".--.-.", "(": "-.--.", ")": "-.--.-"}

morse2text = {value: key.upper() for key, value in text2morse.items()}

line = ''.join([morse2text[i] for i in conn.recvline().strip('\n').strip().split(' ')])

a = {'QIAN': ' --- ', 'DUI': ' --. ', 'LI': ' -.- ', 'ZHEN': ' -.. ', 'XUN': ' .-- ', 'KAN': ' .-. ', 'GEN': ' ..- ', 'KUN': ' ... '}

for i, j in a.items():
	line = line.replace(i, str(j))

line = line.strip().replace('  ', ' ')

conn.sendline(line)

flag = ''.join([morse2text[i] for i in conn.recvuntil("\n").strip('\n').split(' ')])

print(flag)
