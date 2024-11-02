```Python

class SuffixArray:
    def __init__(self, text):
        self.text = text
        self.n = len(text)
        self.suffix_array = self.build_suffix_array()

    def printSuffix(self):
        print(self.suffix_array)

    def build_suffix_array(self):
        suffixes = sorted((self.text[i:], i) for i in range(self.n))
        return [suffix[1] for suffix in suffixes]

    def search(self, pattern):
        # Бинарный поиск по суффиксному массиву
        left, right = 0, self.n
        while left < right:
            mid = (left + right) // 2
            suffix = self.text[self.suffix_array[mid] :]
            if suffix < pattern:
                left = mid + 1
            else:
                right = mid
        start = left

        # Второй бинарный поиск для поиска конца
        left, right = 0, self.n
        while left < right:
            mid = (left + right) // 2
            suffix = self.text[self.suffix_array[mid] :]
            if suffix.startswith(pattern):
                left = mid + 1
            else:
                right = mid

        end = left

        return self.suffix_array[start:end]


# Пример использования
text = "banana"
suffix_array = SuffixArray(text)

print(suffix_array)
pattern = "ana"
result = suffix_array.search(pattern)

print(f"Начальные индексы вхождений '{pattern}': {result}")
```
