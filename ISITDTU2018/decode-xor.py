# step 1: flag first 8 char, get last 8 char of key
# step 2: guess the flag first 10, and change key of last 2
# step 3: get flag

tar='1d14273b1c27274b1f10273b05380c295f5f0b03015e301b1b5a293d063c62333e383a20213439162e0037243a72731c22311c2d261727172d5c050b131c433113706b6047556b6b6b6b5f72045c371727173c2b1602503c3c0d3702241f6a78247b253d7a393f143e3224321b1d14090c03185e437a7a607b52566c6c5b6c034047'

#flag='ISITDTU{xx'*13
flag='ISITDTU{Welcome_to_ISITDTUCTCA]5ntest!_Hav3_a_g05zAaay._Hope_y0u_w1liA-kj0y_and_hav3_a_h4yvZrank_1n_0ur_F1rsqA]qf_C0nt3st._Thank0c'

#key='a'*10
key='xoRCr4cKm3'


guessflag=[0]*130
assert len(key) == 10

if len(flag) % len(key) != 0:
    n = len(key) - len(flag) % len(key)
    for i in range(n):
        flag += " "
m = []
for a in range(10):
    i = a
    for b in range(13):
        cur = int('0x'+tar[2*len(m):2*len(m)+2], 16)
        if b % 2 != 0:
            print '[',len(m),']:',i,'=', chr(cur^ord(key[a])),'^^',a,'=', chr(cur^ord(flag[i]))
            guessflag[i]=chr(cur^ord(key[a]))
            m.append(ord(flag[i]) ^ ord(key[a]))
        else:
            print '[',len(m),']:',i+10-(a+1+a),'=', chr(cur^ord(key[a])), '^', a,'=', chr(cur^ord(flag[i+10-(a+1+a)]))
            guessflag[i+10-(a+1+a)]= chr(cur^ord(key[a]))
            m.append(ord(flag[i+10-(a+1+a)])^ ord(key[a]))
        i += 10
enc_flag = ""
for j in range(len(m)):
    enc_flag += "%02x" % m[j]

print enc_flag
print ''.join(guessflag)
#0d56035b0257035a114300500e5c4f1b015b0f57
#1d14273b1c27274b1f10273b05380c295f5f0b03015e301b1b5a293d063c62333e383a20213439162e0037243a72731c22311c2d261727172d5c050b131c433113706b6047556b6b6b6b5f72045c371727173c2b1602503c3c0d3702241f6a78247b253d7a393f143e3224321b1d14090c03185e437a7a607b52566c6c5b6c034047
#ISITDTU{Welcome_to_ISITDTUCTF_C0ntest!_Hav3_a_g00d_day._Hope_y0u_w1ll_3nj0y_and_hav3_a_h1gh_rank_1n_0ur_F1rst_Ctf_C0nt3st._Thank5}