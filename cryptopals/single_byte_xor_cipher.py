def single_byte_xor(string,key):
        return bytes([i^key for i in string])


hexstring='1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
byte_string=bytes.fromhex(hexstring)
for i in range(0,256):
        print(single_byte_xor(byte_string,i))
