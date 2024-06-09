

iterations = 1561
size_of_flag = 32
remaining = 16

hex_flag = "51124f4d194969633e4b52026f4c07513a6f4d05516e1e50536c4954066a1c57"

byte_data = bytearray.fromhex(hex_flag)

ascii_encrypted_flag = byte_data.decode('utf-8', errors="ignore")

print(49968 * 'a')

print(ascii_encrypted_flag)