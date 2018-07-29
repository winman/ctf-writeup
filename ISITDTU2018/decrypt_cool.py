import itertools
import string
import hashlib 

# Flag Format: ISITDTU{[a-zA-Z0-9_.!?@-]}
flag=['a']*28

# part-1
ok=[0x7D,0x4D,0x23,0x44,0x36,0x02,0x76,0x03,0x6F,0x5B,0x2F,0x46,0x76,0x18,0x39]
'''
^[0:13]=ok[0]
^[0:14]=ok[1]
...
^[0:28]=ok[14]
'''
print len(ok) #15
last=[0]*14
for i in range(len(ok)-1):
  last[-i-1]=chr(ok[-i-1]^ok[-i-2])
  flag[-i-1]=last[-i-1]
print ''.join(last)
#0ngr4tul4ti0n!

# part-2
flag[0xc]=chr(33)
#flag[-15]='c'
print ''.join(flag)

# part-3
#md5[8:12]=BBC86F9D0B90B9B08D1256B4EF76354B
# 20 chars, 14+1+1 known, 4 brute force
# a-zA-Z0-9_.!?@-
mylist=string.ascii_uppercase+string.ascii_lowercase+string.digits+'_.!?@-'
for candidate in itertools.product(mylist, repeat=4):
  for i in range(4):
    flag[8+i]=candidate[i]
  m2 = hashlib.md5()
  test=''
  for i in range(8,12):
     test=test+flag[i]
  m2.update(test)
  #print test, '=>', m2.hexdigest()[0:32]
  if (m2.hexdigest()[0:32] == 'BBC86F9D0B90B9B08D1256B4EF76354B'.lower()):
    print test
    break;

# part-4
#md5[0:4]=ECFD4245812B86AB2A878CA8CB1200F9
#md5[4:8]=88E3E2EDB64D39698A2CC0A08588B5FD
for candidate in itertools.product(mylist, repeat=4):
  for i in range(4):
    flag[4+i]=candidate[i]
  m2 = hashlib.md5()
  test=''
  for i in range(4,8):
     test=test+flag[i]
  m2.update(test)
  if (m2.hexdigest()[0:32] == '88E3E2EDB64D39698A2CC0A08588B5FD'.lower()):
    print test
    break;

for candidate in itertools.product(mylist, repeat=4):
  for i in range(4):
    flag[0+i]=candidate[i]
  m2 = hashlib.md5()
  test=''
  for i in range(0,4):
     test=test+flag[i]
  m2.update(test)
  if (m2.hexdigest()[0:32] == 'ECFD4245812B86AB2A878CA8CB1200F9'.lower()):
    print test
    break;

print ''.join(flag)