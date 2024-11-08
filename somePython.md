## Task

Точка и область На координатной плоскости заданы две области: прямоугольник со сторонами параллельными осям координат, окружность с центром в начале координат. Определите, принадлежит ли данная точка объединению или пересечению областей. Если точка лежит на границе итоговой области, то считается, что она принадлежит ей. Формат входных данных: В единственной строке через пробел перечислены вещественные числа x y x1 y1 x2 y2 r s. x, y – координаты точки x1, y1 – координаты левой нижней вершины прямоугольника x2, y2 – координаты правой верхней вершины прямоугольника r – радиус окружности  s – 0 или 1. 0 – объединение, 1 – пересечение. Формат выходных данных: В единственной строке необходимо вывести True, если точка принадлежит итоговой области, и False в противном случае. ## Solution

```Python
# y = y2 - верхняя длина
# x = x2 - правая ширина
# y = y1 - нижняя длина
# x = x1 - левая ширина
def isInUnion(x,y,x1,y1,x2,y2,r):
    return (x**2+y**2)**0.5 <= r or (y1<=y<=y2 and x1<=x<=x2)


def isInInterception(x,y,x1,y1,x2,y2,r):
    return (x**2+y**2)**0.5<= r and (y1<=y<=y2 and x1<=x<=x2)



x,y,x1,y1,x2,y2,r,s = map(float,input().split())

if not s:
    print(isInUnion(x,y,x1,y1,x2,y2,r))
else:
    print(isInInterception(x,y,x1,y1,x2,y2,r))
```

## Draw task

```Python
import matplotlib.pyplot as plt
import numpy as np

# Coordinates for the points
x, y = [1], [2]  # First point
x1, y1 = [3], [4]  # Second point
x2, y2 = [5], [6]  # Third point
r = 2  # Radius of the circle
x, y, x1, y1, x2, y2, r, s = map(float, input().split())
# Create the plot
plt.figure()

# Plot the points
plt.scatter(x, y, color="red", label="Point 1")
plt.scatter(x1, y1, color="green", label="Point 2")
plt.scatter(x2, y2, color="blue", label="Point 3")

# Plot lines y = y1, y = y2, x = x1, x = x2
plt.axhline(y=y1, color="green", linestyle="--", label=f"y={y1}")
plt.axhline(y=y2, color="blue", linestyle="--", label=f"y={y2}")
plt.axvline(x=x1, color="green", linestyle="--", label=f"x={x1}")
plt.axvline(x=x2, color="blue", linestyle="--", label=f"x={x2}")

# Add coordinate axes (X and Y axes)
plt.axhline(0, color="black", linewidth=1)  # X axis
plt.axvline(0, color="black", linewidth=1)  # Y axis

# Add a circle centered at (0, 0) with radius r
circle = plt.Circle(
    (0, 0), r, color="orange", fill=False, linestyle="-", label=f"Circle radius={r}"
)
plt.gca().add_patch(circle)

# Add labels and title
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Scatter Plot with Lines and Circle")

# Set equal scaling to see the circle as a circle
plt.gca().set_aspect("equal", adjustable="box")

# Display the legend
plt.legend()

# Show the plot
plt.show()
```
