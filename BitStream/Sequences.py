import os


def write_bit_sequence(filename, bit_sequence):
    existing_bits = ""

    if os.path.exists(filename):
        with open(filename, "rb") as f:
            existing_bytes = f.read()
        existing_bits = "".join(f"{byte:08b}" for byte in existing_bytes).rstrip("0")  # Видаляємо зайві нулі

    new_bits = existing_bits + bit_sequence
    byte_list = [int(new_bits[i:i + 8], 2) for i in range(0, len(new_bits), 8)]

    with open(filename, "wb") as f:
        f.write(bytes(byte_list))


def read_bit_sequence(filename, bit_length, offset=0):
    with open(filename, "rb") as f:
        byte_list = list(f.read())

    bit_string = "".join(f"{byte:08b}" for byte in byte_list)
    return bit_string[offset:offset + bit_length]


# Очищаємо файл перед тестуванням
if os.path.exists("bitstream.bin"):
    os.remove("bitstream.bin")

bitstream1 = "100001111"
bitstream2 = "011101110"

write_bit_sequence("bitstream.bin", bitstream1)
write_bit_sequence("bitstream.bin", bitstream2)

b1 = read_bit_sequence("bitstream.bin", 9, 0)
b2 = read_bit_sequence("bitstream.bin", 9, 9)

print(f"b1: {b1}")
print(f"b2: {b2}")
