# complex-rsa

## Description
noob heard that single RSA encryption can be cracked sometimes due to bad implementation, so he encrypted the message twice. See if you can break it.
pubkey1[http://hack.bckdr.in/COMPLEX-RSA/pubkey1]
pubkey2[http://hack.bckdr.in/COMPLEX-RSA/pubkey2]
flag.enc[http://hack.bckdr.in/COMPLEX-RSA/flag.enc]
Created by: Shishir
No. of Correct Submissions: 6

## Solution
Download and check content of files.
```
wget http://hack.bckdr.in/COMPLEX-RSA/pubkey1 && wget http://hack.bckdr.in/COMPLEX-RSA/pubkey12 && wget http://hack.bckdr.in/COMPLEX-RSA/flag.enc
```

We can inspect the public parameters of the keys using the PyCrypto library.

```python
from Crypto.PublicKey import RSA

print '--- pubkey1 ---'
f = open('pubkey1', 'r')
publicKey1 = RSA.importKey(f.read())
print 'N:', publicKey1.n
print 'E:', publicKey1.e
f.close()
print '\n'

print '--- pubkey2 ---'
f = open('pubkey2', 'r')
publicKey2 = RSA.importKey(f.read())
print 'N:', publicKey2.n
print 'E:', publicKey2.e
f.close()
print '\n'
```

Outputs
```
--- pubkey1 ---
N: 554264859105764813308660999731057971935100899008191382001838196926947542874512190874402841957978974562758951331436856029517893995971179950228409634742368823490858553015862605452077729540463185207987338059905256552215054036643656077780363670065154151957507791559734841291875379738678210733333998195096643491711
E: 37507589401


--- pubkey2 ---
N: 554264859105764813308660999731057971935100899008191382001838196926947542874512190874402841957978974562758951331436856029517893995971179950228409634742368823490858553015862605452077729540463185207987338059905256552215054036643656077780363670065154151957507791559734841291875379738678210733333998195096643491711
E: 4268405784672563577566143285906824408738650526784746749170468318123056940297449811287105187623419766934370809781249030117023876215912795037797160740003478418767197450012472858547143622542113157392499087427939336504102036205305906052998841826136038160560099357503377453502865716581429205507834478651

```
So it looks like both public keys have the same n, and pubkey 2 has a really large public exponent. From the description we can assume that the message was encrypted twice, such that
```
c1 = m^e1 (mod N)
c2 = c1^e2 (mod N)
```
We can substitute c1 so that

```
c2 = (m^e1)^e2 (mod N)
c2 = m^(e1*e2) (mod N)
```

A very large public exponent implies significantly small private decryption exponent. This means that we can try to use Wieners attack to obtain the private decryption exponent d.

```python
import owiener

print("--- Wiener's Attack ---")

e = publicKey1.e * publicKey2.e
n = publicKey2.n
d = owiener.attack(e, n)

if d is None:
    print("Failed")
else:
    print("d={}".format(d))

```

Outputs

```
--- Wiener's Attack ---
d=26303119241915216199594566239456133498871761271858884214528771406917554649451

```
Now we got the private exponent!

We can obtain a hexdump from the encrypted flag.enc file as such
```
$ hexdump -ve '1/1 "%.2x"' flag.enc

02acd7d7f075333f571c1e342ccfdee05d9262beef9398e54d25f0c3a72d4817ce61971e546923bf5726299be22fd8a74fba6e39ca6b4c2cac7d88480a10f32c26ab5f84bc772c763094e7d4ad81a4d8b8c03bf19045303713ef53cf162fce89ca73ca6376bd73d808d9e9818a160c6be205591583032871127cbb363946812527
```

Now we simply use that the message in clear, m, = c2^d (mod N).

```python
c = '0x02acd7d7f075333f571c1e342ccfdee05d9262beef9398e54d25f0c3a72d4817ce61971e546923bf5726299be22fd8a74fba6e39ca6b4c2cac7d88480a10f32c26ab5f84bc772c763094e7d4ad81a4d8b8c03bf19045303713ef53cf162fce89ca73ca6376bd73d808d9e9818a160c6be205591583032871127cbb363946812527'

# m = c^d mod n
m = pow(int(c, 0), d, n)
# mh = hex string from obtained number
mh = hex(m)

# Print ascii representation of obtained hex string
print(bytearray.fromhex(mh[2:]).decode())
```

Out comes the flag.


## Useful Resources

https://en.wikipedia.org/wiki/Wiener%27s_attack

https://www.youtube.com/watch?v=OpPrrndyYNU

https://github.com/orisano/owiener
