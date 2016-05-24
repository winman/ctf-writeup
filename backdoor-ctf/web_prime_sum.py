import requests
import string
import re 
import math

def nextPrime(n):
    if (n==1):
        return 2
    m=int(math.sqrt(n))
    def isPrime(x,y):
        if(y==1):
            return True
        elif(x%y==0):
            return False
        else:
            return isPrime(x,y-1)
    if isPrime(n,m):
        return n
    else:
        return nextPrime(n+1)

Target = 'http://hack.bckdr.in/2013-MISC-75/misc75.php'
s = requests.session()  
r = s.get(Target)
match = re.findall(r'First (\d*) prime numbers' , r.content)
sum = 0
curPrime = 0
if match:
    print "Try to SUM up first "+match[0]+" primes"
    for prime in range(0, int(match[0])):
        curPrime = nextPrime(curPrime + 1)
        sum += curPrime
        print "cur is: "+str(curPrime)+", sum: "+str(sum)
print "Result is: "+str(sum)
r =s.post(Target, data={'answer': sum})
print r.content
