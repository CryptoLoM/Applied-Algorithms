class BitSet:
    def __init__(self, size):
        # Розмір множини, кількість цілих чисел (64 біти на кожне число)
        self.size = size
        self.array = [0] * ((size + 63) // 64)

    def insert(self, x):
        # Вставка елемента у множину
        if 0 <= x < self.size:
            self.array[x // 64] |= (1 << (x % 64))

    def delete(self, x):
        # Видалення елемента з множини
        if 0 <= x < self.size:
            self.array[x // 64] &= ~(1 << (x % 64))

    def search(self, x):
        # Пошук елемента у множині
        if 0 <= x < self.size:
            return bool(self.array[x // 64] & (1 << (x % 64)))
        return False

    def clear(self):
        # Очищення множини
        self.array = [0] * ((self.size + 63) // 64)

    def union(self, other):
        # Об'єднання двох множин
        result = BitSet(self.size)
        for i in range(len(self.array)):
            result.array[i] = self.array[i] | other.array[i]
        return result

    def intersection(self, other):
        # Перетин двох множин
        result = BitSet(self.size)
        for i in range(len(self.array)):
            result.array[i] = self.array[i] & other.array[i]
        return result

    def set_difference(self, other):
        # Різниця між множинами (A - B)
        result = BitSet(self.size)
        for i in range(len(self.array)):
            result.array[i] = self.array[i] & ~other.array[i]
        return result

    def sym_difference(self, other):
        # Симетрична різниця між множинами
        result = BitSet(self.size)
        for i in range(len(self.array)):
            result.array[i] = self.array[i] ^ other.array[i]
        return result

    def is_subset(self, other):
        # Перевірка, чи є одна множина підмножиною іншої
        for i in range(len(self.array)):
            if (self.array[i] & other.array[i]) != self.array[i]:
                return False
        return True
