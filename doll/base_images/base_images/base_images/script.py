f = open("flag.txt", "rb")


b = bytearray(f.read())

print(b.decode('ascii'))
