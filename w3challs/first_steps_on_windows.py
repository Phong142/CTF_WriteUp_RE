c1 = [185, 178, 106,  14, 203, 164, 122, 151, 234, 110, 
    237, 216, 130, 201, 225, 113,  47,  56, 125, 123, 
    200, 105, 184, 176, 134, 243,  87,  47, 235, 204, 
    197, 226, 123]
c2 = [238, 129,  41, 117, 156, 151,  22, 244, 218,   3, 
    222, 248, 213, 248, 214,  25,  15, 111,  76,  21, 
    172,  89, 207, 133, 166, 176,  37,  27, 136, 167, 
    168, 209, 6]
for i in range(33):
    print(chr(c1[i]^c2[i]), end = "")

# import string

# array1 = [0xEE, 0x81, 0x29, 0x75, 0x9C, 0x97, 0x16, 0xF4, 0xDA, 0x03, 0xDE,
#           0xF8, 0xD5, 0xF8, 0xD6, 0x19, 0x0F, 0x6F, 0x4C, 0x15, 0xAC, 0x59,
#           0xCF, 0x85, 0xA6, 0xB0, 0x25, 0x1B, 0x88, 0xA7, 0xA8, 0xD1, 0x06, 0x00]

# array2 = [0xB9, 0xB2, 0x6A, 0x0E, 0xCB, 0xA4, 0x7A, 0x97, 0xEA, 0x6E, 0xED,
#           0xD8, 0x82, 0xC9, 0xE1, 0x71, 0x2F, 0x38, 0x7D, 0x7B, 0xC8, 0x69,
#           0xB8, 0xB0, 0x86, 0xF3, 0x57, 0x2F, 0xEB, 0xCC, 0xC5, 0xE2, 0x7B, 0x00]

# i = 0
# flag = ''

# while (i < 0x21):
#     for a in string.printable:
#         if ord(a) ^ array1[i] ^ array2[i] == 0:
#             flag += a
#             i += 1

# print(flag)