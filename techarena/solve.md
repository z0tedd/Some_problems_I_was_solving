# Решение

у нас есть
n нод и m связей
дальше идет число M и F, которые нужны для подсчета стоимости пути в графе
Идет описание массива чисел, которые отображают личную стоимость каждого пути.
и идет кол-во связей в графе.

Основная идея:
делаем из всей этой мешуры взвешанный граф(считаем cost перемещения из одной в точки в другую), проходимся по нему дейкстрой,
схлопываем путь(операция совмещения двух вершин в графе), снова проходимся дейкстрой,
снова схлопываем

План капкан:
делаем из всей этой мешуры взвешанный граф(считаем cost, результирующего графа) -> находим эйлерову цепь. Все

Отмена:
Жадно решение:
Делаем взмвешанный граф -> идем дейкстрой по минимальным ребрам -> вызываем рекурсивно ту же функцию,
только в виде графа у нас смешанный путь, а вместо точки у нас пути смешанной вершины. -> профит