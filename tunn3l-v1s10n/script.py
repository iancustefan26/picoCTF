

with open("tunn3l_v1s10n", "rb") as f:
    b = bytearray(f.read())

print(len(b))


b[23] = 3


with open("modified", "wb") as f:
    f.write(bytes(b))
