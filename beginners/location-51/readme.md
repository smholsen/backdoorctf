# location-51

## Description
n00b after days of exploration found the website where all pro hackers are found dwelling.
He was informed that a flag will be given if behaved properly at that place. Can you find the flag?

Link to the website[http://hack.bckdr.in/LOCATION-51/index.html]. Submit SHA-256 of the flag obtained.
Created by: Ravi Kishore R
No. of Correct Submissions: 843

## Solution

When we try to access the site http://hack.bckdr.in/LOCATION-51/index.html, we instantly get redirected to http://hack.bckdr.in/LOCATION-51/trap.html, where we are asked to input a password. The password is easily obtainable be looking at the javascript.

```javascript
	a = prompt("Password");
	if(a=="H4CK3D")
	{
		alert("Flag is '"+atob("WW91IGFyZSBUcmFwcGVkIDopIFRoaXMgaXMgbm90IHRoZSBmbGFnLiBDaGVjayBhcm91bmQu")+"'");
	}
	else
	{
		alert("Wrong Password!");
	}
```
However, the base64 decoded string from the script is; "You are Trapped :) This is not the flag. Check around."

So lets look again at index.html. We can do this simply by using a js debugging tool to pause any javascript. Or, if you run your traffic through a proxy e.g. Burp Suite, it is probably stored in your sitemap.

The script on this site is
```javascript
a = prompt("Password");
if(a=="H4CK3D")
{
  alert("Flag is "+atob("T0hIX1kwVV9DNE5fQkwwQ0tfSkFWQVNDMVBUICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA"));
}
else
{
  alert("Wrong Password!");
}
```

Decode "T0hIX1kwVV9DNE5fQkwwQ0tfSkFWQVNDMVBUICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA" to UTF-8 to obtain the flag, and submit the sha256sum.
