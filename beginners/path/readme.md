#path

## Description
The flag is somewhere on the domain flag.bckdr.in

Created by: Abhay Bir Singh Rana
No. of Correct Submissions: 650

## Solution
Scanning the domain with any dns recon tool will give you the TXT resource attached to the domain. The flag is stored here.


E.g DNSRecon (https://tools.kali.org/information-gathering/dnsrecon)
```
$ ./dnsrecon.py -d flag.bckdr.in
```
