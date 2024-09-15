class SetOperations:
    def __init__(self):
        # Ініціалізація порожньої множини
        self.set_data = set()

    def insert(self, x):
        # Вставка елемента у множину
        self.set_data.add(x)

    def delete(self, x):
        # Видалення елемента з множини, якщо він існує
        self.set_data.discard(x)

    def search(self, x):
        # Пошук елемента у множині
        return x in self.set_data

    def clear(self):
        # Очищення множини
        self.set_data.clear()

    def union(self, other):
        # Об'єднання двох множин
        result = SetOperations()
        result.set_data = self.set_data.union(other.set_data)
        return result

    def intersection(self, other):
        # Перетин двох множин
        result = SetOperations()
        result.set_data = self.set_data.intersection(other.set_data)
        return result

    def set_difference(self, other):
        # Різниця між множинами (A - B)
        result = SetOperations()
        result.set_data = self.set_data.difference(other.set_data)
        return result

    def sym_difference(self, other):
        # Симетрична різниця між множинами
        result = SetOperations()
        result.set_data = self.set_data.symmetric_difference(other.set_data)
        return result

    def is_subset(self, other):
        # Перевірка, чи є одна множина підмножиною іншої
        return self.set_data.issubset(other.set_data)

    def __repr__(self):
        # Виведення множини як рядок
        return f"SetOperations({self.set_data})"
