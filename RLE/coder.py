def rle_encode(input_file, output_file):
    with open(input_file, "rb") as f_in, open(output_file, "wb") as f_out:
        data = f_in.read()
        if not data:
            return

        compressed = bytearray()
        prev_byte = data[0]
        count = 1

        for byte in data[1:]:
            if byte == prev_byte and count < 255:
                count += 1
            else:
                compressed.extend([count, prev_byte])
                prev_byte = byte
                count = 1
        compressed.extend([count, prev_byte])

        f_out.write(compressed)


