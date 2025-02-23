def rle_decode(input_file, output_file):
    with open(input_file, "rb") as f_in, open(output_file, "wb") as f_out:
        data = f_in.read()
        if not data:
            return

        decompressed = bytearray()

        for i in range(0, len(data), 2):
            count = data[i]
            byte = data[i + 1]
            decompressed.extend([byte] * count)

        f_out.write(decompressed)
