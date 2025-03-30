def bwt_encode(text):
    """Перетворення Барроуза-Вілера (BWT)"""
    if '$' not in text:
        text += '$'  # Додаємо кінцевий символ лише, якщо його немає
    n = len(text)
    # Створення циклічних зсувів
    rotations = [text[i:] + text[:i] for i in range(n)]
    # Лексикографічне сортування
    rotations.sort()
    # Отримання останнього стовпця
    last_column = ''.join(row[-1] for row in rotations)
    # Знаходимо індекс рядка з кінцевим символом '$'
    original_index = rotations.index(text)
    return last_column, original_index

def bwt_decode(bwt_text, original_index):
    """Зворотнє перетворення Барроуза-Вілера (BWT)"""
    n = len(bwt_text)
    table = [''] * n
    for _ in range(n):
        # Додавання стовпця та сортування
        table = sorted([bwt_text[i] + table[i] for i in range(n)])
    # Повертаємо рядок з початковим індексом
    return table[original_index].rstrip('$')

def mtf_encode(text):
    """Move-to-Front кодування"""
    symbols = sorted(set(text))
    encoded = []
    for char in text:
        index = symbols.index(char)
        encoded.append(index)
        # Переміщення символа на початок
        symbols.insert(0, symbols.pop(index))
    return encoded

def mtf_decode(encoded, alphabet):
    """Move-to-Front декодування"""
    symbols = list(alphabet)
    decoded = []
    for index in encoded:
        char = symbols[index]
        decoded.append(char)
        # Переміщення символа на початок
        symbols.insert(0, symbols.pop(index))
    return ''.join(decoded)

def compress(text):
    """Комбінація BWT + MTF"""
    bwt_result, original_index = bwt_encode(text)  # Не додаємо зайвий символ '$'
    mtf_result = mtf_encode(bwt_result)
    return mtf_result, original_index, sorted(set(text + '$'))

def decompress(encoded, original_index, alphabet):
    """Декомпресія BWT + MTF"""
    mtf_decoded = mtf_decode(encoded, alphabet)
    return bwt_decode(mtf_decoded, original_index)

# Тестування
text = "banana"
compressed, original_index, alphabet = compress(text)
print("Стиснене:", compressed)

decompressed = decompress(compressed, original_index, alphabet)
print("Розгорнуте:", decompressed)