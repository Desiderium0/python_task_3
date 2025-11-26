def intersection_area(x1: int, y1: int, x2: int, y2: int, 
                     x3: int, y3: int, x4: int, y4: int) -> int:
    """
    Вычисляет площадь пересечения двух прямоугольников.
    """
    # Проверяем, что прямоугольники имеют положительную площадь
    if x1 >= x2 or y1 <= y2 or x3 >= x4 or y3 <= y4:
        return 0
    
    # Вычисляем пересечение
    x_left = max(x1, x3)
    x_right = min(x2, x4)
    y_bottom = max(y2, y4)  # нижняя граница пересечения
    y_top = min(y1, y3)     # верхняя граница пересечения
    
    # Если пересечение существует
    if x_left < x_right and y_bottom < y_top:
        return (x_right - x_left) * (y_top - y_bottom)
    else:
        return 0

def union_area(x1: int, y1: int, x2: int, y2: int, 
               x3: int, y3: int, x4: int, y4: int) -> int:

    area1 = (x2 - x1) * (y1 - y2)
    area2 = (x4 - x3) * (y3 - y4)

    intersection = intersection_area(x1, y1, x2, y2, x3, y3, x4, y4)
    
    # Площадь объединения = сумма площадей - площадь пересечения
    return area1 + area2 - intersection



if __name__ == "__main__":
    x1, y1, x2, y2 = 0, 2, 4, 1    # Первый прямоугольник
    x3, y3, x4, y4 = 3, 3, 5, 1    # Второй прямоугольник
    print(f"Прямоугольник 1: ЛВ({x1},{y1}) ПН({x2},{y2})")
    print(f"Прямоугольник 2: ЛВ({x3},{y3}) ПН({x4},{y4})")
    print(intersection_area(x1, y1, x2, y2, x3, y3, x4, y4))
    
    x1, y1, x2, y2 = 0, 3, 3, 0
    x3, y3, x4, y4 = 1, 2, 2, 1
    print(f"Вложенные: пересечение = {intersection_area(x1, y1, x2, y2, x3, y3, x4, y4)}")