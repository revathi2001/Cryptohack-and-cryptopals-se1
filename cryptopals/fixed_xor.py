 from pwnlib.util.fiddling import xor

hexstring1='1c0111001f010100061a024b53535009181c'
byte_string1=bytes.fromhex(hexstring1)
hexstring2='686974207468652062756c6c277320657965'
byte_string2=bytes.fromhex(hexstring2)
p=xor(byte_string1,(byte_string2),cut='max')
print(p.hex())
