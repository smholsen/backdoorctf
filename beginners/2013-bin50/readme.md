# 2013-bin-50

## Description
One day, after getting tired of being made fun of by all the other hackers, he decided to finally take a look at BASH.
His first thoughts were 'Bash? Bash Windows? Oh those violent script kiddies!'. After finishing hundreds of online tutorials,
he accidentally (obviously)found a flag. His next status update was ' The script kiddies will never be able to get the flag from this password protected binary.
How dare he call you and us 'script kiddies'?! Take him down.

Here is the file[http://hack.bckdr.in/2013-BIN-50/binary50.zip]. For 32bit users - file[http://hack.bckdr.in/2013-BIN-50/binary50_32bit.zip].
The flag is SHA-256 of the MD-5 hash obtained.

Created by: Ravi Kishore R
No. of Correct Submissions: 1133


## Solution

Download & unzip the file
```
$ wget http://hack.bckdr.in/2013-BIN-50/binary50.zip
$ unzip binary50.zip
```
If we try to run it, it asks us to provide a password.
```
$ ./binaary50
Please provide the password
```
Ok, so lets look for any strings in the binary.

```
$ strings binaary50
...
Password is Advicemallard
qie////3213/wqeqwe/qwqweqsxcf/d/////
Password is Butter
Password is Hoobastank
Password is Darth
Password is Jedimaster
Password is Masternamer
Password is Morpheus
Password is Neutron
Password is Coyote
Password is Tweety
Nothing to see here.
Please provide the password
...
```
If we try all the strings as passords, we will eventually find that Masternamer returns a MD-5 hash.

```
$ ./binaary50 Masternamer
3cd50c6be9bbede06e51741928d88b7e
```
The challenge description tells us that the flag is the 256 hash of the provided MD-5. (Remember that echo always starts with a newline, so use -n to not get that in your hash).
```
$ echo -n 3cd50c6be9bbede06e51741928d88b7e | sha256sum
dad827e94c609b76424287f2523b2117475df29e4ca8475444a9976faedc00f7
```

The flag is dad827e94c609b76424287f2523b2117475df29e4ca8475444a9976faedc00f7
