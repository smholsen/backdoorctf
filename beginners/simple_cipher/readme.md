# simple cipher

## Description
With the help of SDSLabs Mr John encrypted the flag.
The encrypted text can be found here[http://hack.bckdr.in/CPHR/index.php]
Created by: Vishrut Kumar Mishra
No. of Correct Submissions: 441

## Solution

The link leads us to this ciphertext;
```
lkw qlby av qtpfyieidwnpawseycnicsdynjicklqevaciipoksabidpletelbmlpskkupsrrl
```
This looks like a simple substitution cipher, and the first three words looks like "the flag is".
Lets look at the differences and see if we can find a pattern. (I used ASCII values for the calculation)
```
lkw qlby av

the flag is

l - t = 108 - 116 = -8
k - h = 107 - 104 = 3
w - e = 119 - 101 = 18

q - f = 113 - 102 = 11
l - l = 108 - 108 = 0
b - a = 098 - 097 = 1
y - g = 121 - 103 = 18

a - i = 097 - 105 = -8
v - s = 118 - 115 = 3
```

Ok, so we might see a pattern here, meaning this could be a vignere cipher with the key being -8, 3, 18, 11, 0, 1, 18.
Assuming an alphabet of a-z the actual key would be; [26 - 8, 3, 18, 11, 0, 1, 18] = [18, 3, 18, 11, 0, 1, 18]. Encoding this into an alphabet key, we get the word sdslabs.

Lets try it here; http://www.mygeocachingprofile.com/codebreaker.vigenerecipher.aspx
```
Alphabet: ABCDEFGHIJKLMNOPQRSTUVWXYZ
Cipher Key: sdslabs
```

the decoded message reveals the flag.
