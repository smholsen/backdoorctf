# undisputed

## Description
n00b found a file somewhere in the proland. Search this file[http://hack.bckdr.in/UNDISPUTED/file.ext4] to find the flag. Submit SHA-256 of the flag obtained.
Created by: Amanpreet Singh
No. of Correct Submissions: 772

## Solution
Download the file and verify the extension before we mount it and inspect it.
```
$ wget http://hack.bckdr.in/UNDISPUTED/file.ext4
$ file file.ext4
file.ext4: Linux rev 1.0 ext4 filesystem data, UUID=088c23fa-b15c-4439-b709-990571544124 (extents) (huge files)
$ sudo mount file.ext4 .
```
Now lets inspect the noob.7z file inside.

```
$ 7z x n00b.7z

7-Zip [64] 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18
p7zip Version 9.20 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,4 CPUs)

Processing archive: n00b.7z

Extracting  n00b/n00b.txt
Extracting  n00b

Everything is Ok

Folders: 1
Files: 1
Size:       28

```

Now simply look inside the n00b.txt file, generate the sha256sum of the content, and you got your flag.

```
$ echo -n like_a_walk_in_a_park | sha256sum
```
