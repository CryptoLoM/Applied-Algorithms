from coder import  rle_encode
from decoder import rle_decode
def main():
    input_file = "скала.jpg"  # Вхідний файл
    compressed_file = "скала.rle"  # Стиснений файл
    decompressed_file = "відновлена_скала.jpg"  # Відновлений файл

    # Виконати стиснення
    rle_encode(input_file, compressed_file)
    print(f"Файл {input_file} успішно стиснено у {compressed_file}")

    # Виконати розпакування
    rle_decode(compressed_file, decompressed_file)
    print(f"Файл {compressed_file} успішно розпаковано у {decompressed_file}")

if __name__ == "__main__":
    main()