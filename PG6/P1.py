import math

# Ввод координат и радиусов кругов
x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

# Вычисление расстояния между центрами кругов
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Добавляем небольшое значение для компенсации погрешности
epsilon = 1e-9

# Проверка условий пересечения или касания кругов
if distance <= r1 + r2 + epsilon and distance >= abs(r1 - r2) - epsilon:
    print("YES")
else:
    print("NO")
