import base64
import string

ciphertext = base64.b64decode("2xv1pdJYc54wu4Q+YJeRAMc10dOc2Ragr0Fb3YpOv/4=")

plaintext1 = b'Texp8BQv'
all_string = string.digits + string.ascii_letters

for i in all_string:
    for j in all_string:
        for k in all_string:
            iv = key = "ZeroA" + i + j + k
            des = DES.new(key, DES.MODE_CBC, iv)
            plaintext = des.decrypt(ciphertext)
            if plaintext.startswith(b'Texp8BQv'):
                print(plaintext)