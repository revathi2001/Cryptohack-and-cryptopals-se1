from pwnlib.util.fiddling import xor

plain=b"""Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
key=b'ICE'*24+b'IC'
print(xor(key,(plain),cut='max').hex())
