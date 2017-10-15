# browser

## Description
This one is pretty easy. Here[http://hack.bckdr.in/BRWSR] is the link of the page where the flag is there. This page opens only in a specific browser which is developed by the folks of SDSLabs. But unfortunately this browser is only availiable for internal use. See if you can find the flag...

Created by: Dhaval Kapil
No. of Correct Submissions: 1003

## Solution

The server verifies that the client is using the internal SDSLabs browser by looking at the User-Agent field in the HTTP Header. This was simply a guess from the challenge description.

I used Burp Suite to set up a proxy and intercept and edit the request.

```
GET /BRWSR/ HTTP/1.1
Host: hack.bckdr.in
User-Agent: SDSLabs
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
```

This returned the following response.

```
HTTP/1.1 200 OK
Date: Sun, 15 Oct 2017 18:43:36 GMT
Server: Apache/2.4.18 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 210
Connection: close
Content-Type: text/html; charset=UTF-8


<html>
	<head>
		<title>
		</title>
	<head>
	<body>
		<div>Welcome!! Thanks for using our browser! Here's a flag for you: e77aec24943bb31c63547812d1130c67d0e7e941bf5d85bfef0492cc68050aef</div>
	</body>
</html>
```
