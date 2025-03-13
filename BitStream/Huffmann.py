import heapq
from collections import defaultdict


class HuffmanNode:
    def __init__(self, byte, freq):
        self.byte = byte
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_frequency_table(filename):
    freq_table = defaultdict(int)
    with open(filename, "rb") as f:
        byte = f.read(1)
        while byte:
            freq_table[byte] += 1
            byte = f.read(1)
    return freq_table


def build_huffman_tree(freq_table):
    priority_queue = [HuffmanNode(byte, freq) for byte, freq in freq_table.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0] if priority_queue else None


def build_huffman_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}

    if node:
        if node.byte is not None:
            codebook[node.byte] = prefix
        build_huffman_codes(node.left, prefix + "0", codebook)
        build_huffman_codes(node.right, prefix + "1", codebook)

    return codebook


def save_compressed_file(input_filename, output_filename, codebook, freq_table):
    with open(input_filename, "rb") as f_in, open(output_filename, "wb") as f_out:
        # Збереження таблиці частот (записуємо тільки наявні символи)
        f_out.write(len(freq_table).to_bytes(2, byteorder="big"))  # Кількість унікальних символів
        for byte, freq in freq_table.items():
            f_out.write(byte)  # Сам байт (1 байт)
            f_out.write(freq.to_bytes(4, byteorder="big"))  # Частота (4 байти)

        # Кодування файлу
        bit_string = ""
        byte = f_in.read(1)
        while byte:
            bit_string += codebook[byte]
            byte = f_in.read(1)

        # Додаємо біти для вирівнювання
        padding_size = (8 - len(bit_string) % 8) % 8
        bit_string += "0" * padding_size
        f_out.write(bytes([padding_size]))

        # Записуємо бітові дані у файл
        byte_array = bytearray()
        for i in range(0, len(bit_string), 8):
            byte_array.append(int(bit_string[i:i + 8], 2))
        f_out.write(byte_array)


def load_compressed_file(input_filename, output_filename):
    with open(input_filename, "rb") as f_in:
        # Читаємо кількість унікальних символів
        num_symbols = int.from_bytes(f_in.read(2), byteorder="big")

        # Читаємо таблицю частот
        freq_table = {}
        for _ in range(num_symbols):
            byte = f_in.read(1)
            freq = int.from_bytes(f_in.read(4), byteorder="big")
            freq_table[byte] = freq

        # Відновлення дерева Хаффмана
        root = build_huffman_tree(freq_table)
        if not root:
            return

        # Читаємо відступ (padding)
        padding_size = int.from_bytes(f_in.read(1), byteorder="big")

        # Читаємо всі бітові дані
        bit_string = ""
        byte = f_in.read(1)
        while byte:
            bit_string += f"{int.from_bytes(byte, byteorder='big'):08b}"
            byte = f_in.read(1)

        # Видаляємо додаткові нулі
        bit_string = bit_string[:-padding_size] if padding_size > 0 else bit_string

        # Декодування
        decoded_bytes = bytearray()
        node = root
        for bit in bit_string:
            node = node.left if bit == "0" else node.right
            if node.byte is not None:
                decoded_bytes.append(node.byte[0])  # Виправлена помилка

                # Повертаємось до кореня дерева
                node = root

        # Записуємо результат у файл
        with open(output_filename, "wb") as f_out:
            f_out.write(decoded_bytes)



input_file = "Лаб 1.docx"
compressed_file = "compressed.Лаб 1.docx"
decompressed_file = "output.Лаб 1.docx"


freq_table = build_frequency_table(input_file)
huffman_tree = build_huffman_tree(freq_table)
huffman_codes = build_huffman_codes(huffman_tree)

save_compressed_file(input_file, compressed_file, huffman_codes, freq_table)
load_compressed_file(compressed_file, decompressed_file)

