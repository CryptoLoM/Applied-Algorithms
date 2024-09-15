class SetOperations:
    def __init__(self, t):
        # Ініціалізація масиву 64-розрядних регістрів
        self.size = t
        self.set_data = [0] * t  # Масив з t регістрів (кожен з них - 64 біти)

    def _get_index(self, x):
        # Отримання індексу в масиві і позиції біта
        if x < 0 or x >= 64 * self.size:
            return None  # Повертаємо None для випадків виходу за межі
        return x // 64, x % 64

    def insert(self, x):
        # Вставка елемента в множину
        index_position = self._get_index(x)
        if index_position is not None:
            index, bit_position = index_position
            self.set_data[index] |= (1 << bit_position)

    def delete(self, x):
        # Видалення елемента з множини
        index_position = self._get_index(x)
        if index_position is not None:
            index, bit_position = index_position
            self.set_data[index] &= ~(1 << bit_position)

    def search(self, x):
        # Пошук елемента в множині
        index_position = self._get_index(x)
        if index_position is None:
            return False  # Повертаємо False, якщо елемент виходить за межі
        index, bit_position = index_position
        return (self.set_data[index] & (1 << bit_position)) != 0

    def clear(self):
        # Очищення множини
        self.set_data = [0] * self.size

    def union(self, other):
        # Об'єднання двох множин
        result = SetOperations(self.size)
        for i in range(self.size):
            result.set_data[i] = self.set_data[i] | other.set_data[i]
        return result

    def intersection(self, other):
        # Перетин двох множин
        result = SetOperations(self.size)
        for i in range(self.size):
            result.set_data[i] = self.set_data[i] & other.set_data[i]
        return result

    def set_difference(self, other):
        # Різниця між множинами (A - B)
        result = SetOperations(self.size)
        for i in range(self.size):
            result.set_data[i] = self.set_data[i] & ~other.set_data[i]
        return result

    def sym_difference(self, other):
        # Симетрична різниця між множинами
        result = SetOperations(self.size)
        for i in range(self.size):
            result.set_data[i] = self.set_data[i] ^ other.set_data[i]
        return result

    def is_subset(self, other):
        # Перевірка, чи є одна множина підмножиною іншої
        for i in range(self.size):
            if (self.set_data[i] & ~other.set_data[i]) != 0:
                return False
        return True

    def __repr__(self):
        # Виведення множини як рядок
        return f"SetOperations({self.set_data})"
