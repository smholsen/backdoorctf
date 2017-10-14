import httplib


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


# Create an http connection and obtain the amount of primes we need
conn = httplib.HTTPConnection("hack.bckdr.in")
conn.request("GET", 'http://hack.bckdr.in/2013-MISC-75/misc75.php')
res = conn.getresponse()
completePage = res.read()

# We only want the second number. (You Have 3 seconds to solve this question . Find the sum of First 1115 prime numbers .)
firstword = True
for word in completePage.split(" "):
    if word.isdigit():
        if not firstword:
            n = int(word)
        firstword = False

print 'Finding sum for ', n
answer = find_sum(n)
print 'sum is', answer

# We must include the cookie in our crafted response, aswell as the Content-type
cookie = res.getheaders()[1][1]
print cookie
header = {
    'Content-type': 'application/x-www-form-urlencoded',
	'Cookie': cookie
}

# Send the answer as post form data "answer"
parameters = 'answer='+str(answer)
conn.request("POST", 'http://hack.bckdr.in/2013-MISC-75/misc75.php', parameters, header)
res = conn.getresponse()
print res.read()
