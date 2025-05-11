s1 = 'hello, world!'
s2 = "你好，世界！❤️"
s3 = '''hello,
wonderful
world!'''
print(s1)
print(s2)
print(s3)

# s1 = '\it \is \time \to \read \now'
s2 = r'\it \is \time \to \read \now'
# print(s1)
print(s2)

s1 = '\141\142\143\x61\x62\x63'
s2 = '\u5f20\u61cb'
print(s1)
print(s2)

s = 'abc123456'
print(s[-7:-4])       # c12
print(s[2:])          # c123456
print(s[:2])          # ab
print(s[::2])         # ac246
print(s[::-1])        # 654321cba
