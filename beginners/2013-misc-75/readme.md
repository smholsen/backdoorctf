# 2013-misc-75

## Description
H4x0r once proclaimed on his posterous blog, ' Time eventually catches up with everyone , but not H4x0r. Challenge me if you can !'
Time to bring him down to his Win98 world .

Here is the link[http://hack.bckdr.in/2013-MISC-75/misc75.php]

Created by: Ravi Kishore R
No. of Correct Submissions: 549


## Solution
By Inspecting the provided site we can see that we are tasked to calculate the sum of the n first primes where n is provided. We must then send our result within 3 seconds.

We can inspect the network traffic in our browser and see that the form is sent as a POST request and that it contains a parameter "answer" with our input. We can use this to programatically craft and send a response. The site gives us a cookie that is renewed on every refresh.

To solve the challenge I used the python library httplib.

We can get the initial site by requesting it and reading it.
 ```python
 # Create an http connection and obtain the amount of primes we need
 conn = httplib.HTTPConnection("hack.bckdr.in")
 conn.request("GET", 'http://hack.bckdr.in/2013-MISC-75/misc75.php')
 res = conn.getresponse()
 completePage = res.read()
 ```
We must then parse our response to obtain the number of primes we need to sum.

```python
# We only want the second number. (You Have 3 seconds to solve this question . Find the sum of First 1115 prime numbers .)
firstword = True
for word in completePage.split(" "):
    if word.isdigit():
        if not firstword:
            n = int(word)
        firstword = False
```

We can then find the sum like this;
```python
def is_prime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def find_sum(n_first):
    sum = 0
    i = 0
    cnt = 2
    while (i < n_first):
        if is_prime(cnt):
            sum = sum + cnt
            i += 1
        cnt += 1
    return sum

answer = find_sum(n)
```

When we have our answer we can craft our response. We must remember to include the cookie provided in the previous response.

```python
# We must include the cookie in our crafted response, aswell as the Content-type
cookie = res.getheaders()[1][1]
header = {
  'Content-type': 'application/x-www-form-urlencoded',
  'Cookie': cookie
}
```

We then send it and look at what we get back.
```python
# Send the answer as post form data "answer"
parameters = 'answer='+str(answer)
conn.request("POST", 'http://hack.bckdr.in/2013-MISC-75/misc75.php', parameters, header)
res = conn.getresponse()
print res.read()
```
Output: Congratulations! You passed it . Your award ==> 2ac4a6e921c6a5f5f36e8300896b597f9b4f83dc197294ca39fc3a862c734856
