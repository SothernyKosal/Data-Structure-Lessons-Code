from decimal import Decimal


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


p = int(input('Enter the value of p = '))
q = int(input('Enter the value of q = '))
no = int(input('Enter the value of text = '))
n = p * q
theta = (p - 1) * (q - 1)

# 1<e<theta, gcd(e,t)=1
# e : encrytion key
for e in range(2, theta):
    if gcd(e, theta) == 1:
        break

for i in range(1, 10):
    x = 1 + i * theta
    if x % e == 0:
        # decrytion key
        d = int(x / e)
        break
ctt = Decimal(0)
ctt = pow(no, e)
ct = ctt % n

dtt = Decimal(0)
dtt = pow(ct, d)
dt = dtt % n

print(' n = ' + str(n) + '\n encryption key,e = ' + str(e) + '\n theta = ' + str(theta) + '\n decryption key, d = ' + str(d) + '\n cipher text = ' + str(
    ct) + '\n decrypted text = ' + str(dt))