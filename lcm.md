Конструкция `count_ab = n // lcm(a, b)` встречается при решении задач, связанных с подсчетом чисел, которые делятся одновременно на два числа \( a \) и \( b \). Давай разберемся, что это значит и как связаны общие делители и наименьшее общее кратное (LCM, Least Common Multiple).

### 1. Что значит `n // lcm(a, b)`?

Это выражение определяет количество чисел от 1 до \( n \), которые делятся на оба числа \( a \) и \( b \). Формула `n // lcm(a, b)` означает:

- `lcm(a, b)` — это наименьшее общее кратное двух чисел \( a \) и \( b \).
- `n // lcm(a, b)` — целочисленное деление количества чисел от 1 до \( n \) на `lcm(a, b)`.

Таким образом, `n // lcm(a, b)` возвращает количество чисел от 1 до \( n \), которые делятся и на \( a \), и на \( b \).

### 2. Как это связано с общими делителями?

Под "количеством общих делителей" можно понимать, сколько чисел одновременно делятся на \( a \) и \( b \). Однако здесь более точно говорить о "числах, кратных обоим". Эти числа обязательно делятся на наименьшее общее кратное \( lcm(a, b) \).

Если мы рассматриваем числа, делящиеся одновременно на \( a \) и \( b \), то вместо проверки делимости каждого из них и на \( a \), и на \( b \) (что сложно), достаточно проверить делимость на их \( lcm(a, b) \), так как это кратное гарантированно будет делиться и на \( a \), и на \( b \).

### 3. Почему работает эта формула?

Если мы хотим посчитать, сколько чисел от 1 до \( n \) делятся одновременно на \( a \) и \( b \), важно учитывать, что такие числа встречаются с шагом, равным \( lcm(a, b) \). Таким образом, при делении `n // lcm(a, b)` мы находим, сколько раз кратное обоим \( a \) и \( b \) число "умещается" в пределах от 1 до \( n \).

### Пример

Предположим:

- \( n = 30 \)
- \( a = 4 \)
- \( b = 6 \)

1. Найдем \( lcm(4, 6) = 12 \).
2. Теперь используем формулу: \( 30 // 12 = 2 \), то есть два числа от 1 до 30 делятся и на 4, и на 6 (12 и 24).

Это и есть ответ: количество чисел от 1 до 30, которые делятся на оба числа, равно 2.

### Итог

Формула `count_ab = n // lcm(a, b)` помогает быстро находить количество чисел, делящихся одновременно на \( a \) и \( b \), без необходимости проверять каждое число вручную.
