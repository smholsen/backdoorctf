# lost

## Description
Recently, n00b got hands on a flag in hackland, but competition is fierce. n00b lost his flag to pro people somewhere in the hackland. Help him recover it here[http://hack.bckdr.in/LOST]
Created by: Amanpreet Singh
No. of Correct Submissions: 1017

## Solution
Lets visit the site. It tells us the following
```
Hi! Welcome to Web-50!

Flag is somewhere around and simple to get, just sneak well in console.
```

Looking at the output in the console we can see two console logs
```
Welcome n00b to the ctf
n00b sometimes you need to POST to flag.php
```

It tells us we need to send a POST request to flag.php.
Lets set up a proxy with burpSuite so we can change the requests on the fly.

 We can now try to access ```http://hack.bckdr.in/LOST/flag.php``` via our broswers and intercept the request with burpsuite.

Lets change the GET to POST and forward the request.

```
POST /LOST/flag.php HTTP/1.1
Host: hack.bckdr.in
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
```

Forward the message and the flag is in the response.
