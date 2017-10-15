# file reader

## Description
An amateur made a simple web app and hid the flag somewhere. Go find it here[http://hack.bckdr.in/FLREAD/].

Created by: Dhaval Kapil
No. of Correct Submissions: 1072

## Solution
The url points us to a site contianing a further url to a directory tree. If we visit the parent directory we can see file called "flag.php". Trying to access it directly doesnt return anything.

There is a directory called "viewer/", which contains a file called "viewer.php". The viewer.php file allows the user to input the path of a file on the server to print it. Simply input the path to the flag, and there it is.

I first tried the path
```
"../flag.php"
```
, which returned
```
./flag.php : No such file exists
```
I'm not sure why the first . is stripped away,but just adding a third . did the trick.

```
<?php
	$flag = "93b9e8c732573769fac43d744fad4120bde8d1f98cc1f6e9011045ff72f45b96";
?>
```
