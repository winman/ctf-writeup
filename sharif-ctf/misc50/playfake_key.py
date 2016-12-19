from random import randint, choice
from string import ascii_uppercase
from hashlib import md5
#from secret import msg, key

import itertools
def bruteforce(charset, length):
    return (''.join(candidate)
        for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
        for i in range(length, length + 1)))

def bruteforce2(charset, length):
    return list(map("".join, itertools.permutations(charset, length)))		
		
#bfstr=list(bruteforce(ascii_uppercase, 5))
bfstr=bruteforce2(ascii_uppercase,5)

#msg='SharifCTF is a contest'
#key='TESTM'

#assert (len(key) == 5) and key.isalpha() and key.isupper()

# "msg" is a meaningful English sentence.
#assert all(x.isalpha() or x.isspace() for x in msg)
#assert "SharifCTF" in msg
#assert "contest" in msg

LIN = 'B'
LOUT = 'P'
 
def make_key(key_str):
	key_str += ascii_uppercase
	key_str = key_str.replace(' ', '').upper().replace(LIN, LOUT)

	seen = set()
	seen_add = seen.add
	return [x for x in key_str if not (x in seen or seen_add(x))]
 
 
def get_pos(key, letter):
	i = key.index(letter)
	return (i//5, i%5)

def get_letter(key, i, j):
	i %= 5
	j %= 5
	return key[5*i + j]
 
def make_message(msg):
	msg = msg.replace(' ', '').upper().replace(LIN, LOUT)
	outp = ''
	i = 0
	while True:
		if i+1 >= len(msg):
			if i == len(msg)-1:
				outp += msg[i]
			break
		if msg[i] == msg[i+1]:
			outp += msg[i] + 'Y'
			i += 1
		else:
			outp += msg[i] + msg[i+1]
			i += 2
	if len(outp) % 2 == 1:
		outp += 'Y'
	return outp
 
def playfair_enc(key, msg):
	assert len(msg) % 2 == 0
	assert len(key) == 25
	ctxt = ''
	for i in range(0, len(msg), 2):
		r0, c0 = get_pos(key, msg[i])
		r1, c1 = get_pos(key, msg[i+1])
		if r0 == r1:
			ctxt += get_letter(key, r0+1, c0+1) + get_letter(key, r1+1, c1+1)
		elif c0 == c1:
			ctxt += get_letter(key, r0-1, c0-1) + get_letter(key, r1-1, c1-1)
		else:
			ctxt += get_letter(key, r0+1, c1-1) + get_letter(key, r1+1, c0-1)
	return ctxt


def make_flag(msg):
	return 'SharifCTF{%s}' % md5(msg.replace(' ', '').upper().encode('ASCII')).hexdigest()
 
if __name__ == '__main__':
	for key in bfstr:
		check=0
		keybackup = key
		key = make_key(key)
		msg='SharifCT'
		msg2 = make_message(msg)
		ctxt = playfair_enc(key, msg2)
		if ctxt in 'KPDPDGYJXNUSOIGOJDUSUQGFSHJUGIEAXJZUQVDKSCMQKXIR':
			#print keybackup, "-1-", ctxt
			check = check+1
		msg='harifCTF'
		msg2 = make_message(msg)
		ctxt = playfair_enc(key, msg2)
		if ctxt in 'KPDPDGYJXNUSOIGOJDUSUQGFSHJUGIEAXJZUQVDKSCMQKXIR':
			#print keybackup, "-2-", ctxt
			check = check+1
		msg='contes'
		msg2 = make_message(msg)
		ctxt = playfair_enc(key, msg2)
		if ctxt in 'KPDPDGYJXNUSOIGOJDUSUQGFSHJUGIEAXJZUQVDKSCMQKXIR':
			#print keybackup, "-3-", ctxt
			check = check+1
		msg='ontest'
		msg2 = make_message(msg)
		ctxt = playfair_enc(key, msg2)
		if ctxt in 'KPDPDGYJXNUSOIGOJDUSUQGFSHJUGIEAXJZUQVDKSCMQKXIR':
			#print keybackup, "-4-", ctxt
			check = check+1
		if check==2:
			print keybackup, '=', check
		#print(ctxt)		# KPDPDGYJXNUSOIGOJDUSUQGFSHJUGIEAXJZUQVDKSCMQKXIR
	
	# Notice that flag is generated using "msg", not "msg2".
	# After decryption, you get "msg2".
	# You must manually add spaces and perform other required changes to get "msg".
	flag = make_flag(msg)
	print(flag)