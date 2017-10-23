from Cryptodome import PublicKey
from Cryptodome.PublicKey import RSA
import owiener


print('--- pubkey1 ---')
f = open('pubkey1', 'r')
publicKey1 = PublicKey.RSA.import_key(f.read())
print('N:', publicKey1.n)
print('E:', publicKey1.e)
f.close()
print('\n')

print('--- pubkey2 ---')
f = open('pubkey2', 'r')
publicKey2 = PublicKey.RSA.importKey(f.read())
print('N:', publicKey2.n)
print('E:', publicKey2.e)
f.close()
print('\n')

print("--- Wiener's Attack ---")

e = publicKey1.e * publicKey2.e
n = publicKey2.n
d = owiener.attack(e, n)

if d is None:
    print("Failed")
else:
    print("Hacked d={}".format(d))

c = '0x02acd7d7f075333f571c1e342ccfdee05d9262beef9398e54d25f0c3a72d4817ce61971e546923bf5726299be22fd8a74fba6e39ca6b4c2cac7d88480a10f32c26ab5f84bc772c763094e7d4ad81a4d8b8c03bf19045303713ef53cf162fce89ca73ca6376bd73d808d9e9818a160c6be205591583032871127cbb363946812527'

# m = c^d mod n
m = pow(int(c, 0), d, n)
mh = hex(m)

print(bytearray.fromhex(mh[2:]).decode())