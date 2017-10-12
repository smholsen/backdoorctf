# 2013-web-50

## Description
H4x0r, in his early days, made an authentication system. He obviously felt that he had the made the most cutting-edge system but we know how brilliant he actually is. Show him just how easy it is to become the admin. You can visit this link [http://hack.bckdr.in/2013-WEB-50/getflag.php] to get the flag once you become admin.

Created by: Ravi Kishore R
No. of Correct Submissions: 2039

## Solution
Visiting the link we are met with a website containing the string; "You are not admin".

Inspecting the cookie we can see that it contains "username=john". Let's try and change that to "username=admin", and refresh the site.
```
document.cookie="username=admin"
```
The flag is 9826f65d07b8861bfad0aba3be5e5f4a4207d1c850527f4d3a2266eca4965de3
