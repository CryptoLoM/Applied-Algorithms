from Huffmann import HuffmanNode, build_huffman_tree,build_huffman_codes
from collections import  defaultdict
import struct

# Функція стиснення (кодування) LZW
def lzw_compress(input_data):
    max_table_size = 256  # байтовий алфавіт
    dictionary = {bytes([i]): i for i in range(max_table_size)}

    string = b""
    compressed_data = []

    for symbol in input_data:
        new_string = string + bytes([symbol])
        if new_string in dictionary:
            string = new_string
        else:
            compressed_data.append(dictionary[string])
            if len(dictionary) < 4096:  # Обмеження розміру словника
                dictionary[new_string] = len(dictionary)
            string = bytes([symbol])

    if string:
        compressed_data.append(dictionary[string])

    return compressed_data


# Функція розпакування (декодування) LZW
def lzw_decompress(compressed_data):
    max_table_size = 256
    dictionary = {i: bytes([i]) for i in range(max_table_size)}

    string = dictionary[compressed_data.pop(0)]
    decompressed_data = bytearray(string)

    for code in compressed_data:
        if code in dictionary:
            entry = dictionary[code]
        elif code == len(dictionary):
            entry = string + string[:1]
        else:
            raise ValueError("Invalid compressed data")

        decompressed_data.extend(entry)

        if len(dictionary) < 4096:
            dictionary[len(dictionary)] = string + entry[:1]

        string = entry

    return decompressed_data


# Збереження стиснених даних у файл
def save_compressed_file(input_filename, output_filename):
    with open(input_filename, "rb") as f_in:
        input_data = f_in.read()
    compressed_data = lzw_compress(input_data)
    with open(output_filename, "wb") as f_out:
        for num in compressed_data:
            f_out.write(num.to_bytes(2, byteorder="big"))


# Завантаження та розпакування файлу
def load_decompressed_file(input_filename, output_filename):
    with open(input_filename, "rb") as f_in:
        compressed_data = []
        while byte := f_in.read(2):
            compressed_data.append(int.from_bytes(byte, byteorder="big"))
    decompressed_data = lzw_decompress(compressed_data)
    with open(output_filename, "wb") as f_out:
        f_out.write(decompressed_data)



# Використання
input_file = "la.txt"
compressed_file = "compressedLZW.la.txt"
decompressed_file = "outputLZW.la.txt"

save_compressed_file(input_file, compressed_file)
load_decompressed_file(compressed_file, decompressed_file)