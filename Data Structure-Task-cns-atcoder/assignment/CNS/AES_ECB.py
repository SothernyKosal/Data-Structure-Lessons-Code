# AES 128 in ECB mode
# from Crypto.Cipher import AES
#
# key = "abcdefghijklmnop"
# cipher = AES.new(key, AES.MODE_EBC)
# msg = cipher.encrypt('TechTutorialsX!!TechTutorialsX!!')
# print(type(msg))
#
# print(msg.encode("hex"))
#
# decipher = AES.new(key, AES.MODE_ECB)
# print(decipher.decrypt(msg))

KEY = "8d2e60365f17c7df1040d7501b4a7b5a"
PLAINTEXT = "59b5088e6dadc3ad5f27a460872d5929"
CT=""
KEY[0] = KEY
PLAINTEXT[0] = PLAINTEXT
for i in range(0,99):
    # print(KEY[i])
    # print(PLAINTEXT[0])
    for j in range(0,999):
        CT[j]  =  encrypt(KEY[I], )
