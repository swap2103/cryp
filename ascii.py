import base64

#7-bit encoding standard which allows the representation of text using the integers 0-127
ascii_encoding = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

#In Python, the chr() function can be used to convert an ASCII ordinal number to a character (the ord() function does the opposite).
temp=""
for i in ascii_encoding:
    temp = temp + str(chr(i))
print(temp)

#output: crypto{ASCII_pr1nt4bl3}

#type(ciphertext) -> We want it to be Numerical
# Because we want it to be transferrable (to differnt systems)

#what do we know
#   -Ascii is a encoding scheme that represents symbols and alphabets in a 7 bit numerical system
'''
How is Ascii utilized by computing systems ?
abc -> 100101

32 bit system
computing system as well as the data both are treated as 32-bit values and objects

Keyboard Driver
Key 15 is what ?
Key | bit value | chr (A)

Answer:
Encoding shcemes
protocols 
all these are always plurals these are designed to help two computers communicate
'''

hex_string = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

# abc -> 616263 -> hex(616263)

byt=bytes.fromhex(hex_string)
print(byt)
byt_flag_string=b'crypto{You_will_be_working_with_hex_strings_a_lot}'
str_flag_string="crypto{You_will_be_working_with_hex_strings_a_lot}"

hex_flag_string=""
for i in str_flag_string:
    #print(i)
    hex_flag_string=hex_flag_string+str(hex(ord(i))[2:])
'''
issue:

'''
print(byt_flag_string.hex())
print(hex_flag_string)

bas_64_hex="72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

#print("hex to bytes=",bytes.fromhex(bas_64_hex))
byt_bas_64 = bytes.fromhex(bas_64_hex)

print("base 64 value=",base64.b64encode(byt_bas_64))

'''
test_hex_string = "1a2b3c"
bytes_result = bytes.fromhex(test_hex_string)
 
print(type(test_hex_string))
print(bytes_result)

the print byte itself results in an ascii/utf encoded value b'\x1a+<'
'''