def intersection_area(ax1: int, ay1: int, ax2: int, ay2: int, 
                     bx1: int, by1: int, bx2: int, by2: int) -> int:
    """
    Вычисляет площадь пересечения двух прямоугольников.
    
    Аргументы:
    ax1, ay1 - левый верхний угол первого прямоугольника
    ax2, ay2 - правый нижний угол первого прямоугольника
    bx1, by1 - левый верхний угол второго прямоугольника  
    bx2, by2 - правый нижний угол второго прямоугольника
    """
    # Положительную площадь у прямоугольника
    if ax1 >= ax2 or ay1 <= ay2 or bx1 >= bx2 or by1 <= by2:
        return 0

    x_left = max(ax1, bx1)
    x_right = min(ax2, bx2)
    y_top = min(ay1, by1)
    y_bottom = max(ay2, by2)
    
    # Если пересечение существует
    if x_left < x_right and y_bottom < y_top:
        return (x_right - x_left) * (y_top - y_bottom)
    else:
        return 0

def union_area(ax1: int, ay1: int, ax2: int, ay2: int, 
               bx1: int, by1: int, bx2: int, by2: int) -> int:
    """
    Вычисляет площадь объединения двух прямоугольников.
    """
    area1 = (ax2 - ax1) * (ay1 - ay2) # Первый прямоугольник
    area2 = (bx2 - bx1) * (by1 - by2) # Второй прямоугольник
    intersection = intersection_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
    
    return area1 + area2 - intersection

def main(ax1: int, ay1: int, ax2: int, ay2: int, 
        bx1: int, by1: int, bx2: int, by2: int):
    print("Программа для вычисления площадей прямоугольников")
    print("Формат: левый верхний угол (x1,y1), правый нижний (x2,y2)")
    print("Для выхода введите 'q'")
    
    while True:
        try:
            # Первый прямоугольник
            coords1 = input("\nВведите координаты первого прямоугольника (x1 y1 x2 y2): ")
            if coords1.lower() == 'q':
                break
                
            ax1, ay1, ax2, ay2 = map(int, coords1.split())
            
            # Второй прямоугольник
            coords2 = input("Введите координаты второго прямоугольника (x1 y1 x2 y2): ")
            if coords2.lower() == 'q':
                break
                
            bx1, by1, bx2, by2 = map(int, coords2.split())
            
            # Проверка корректности
            if ax1 >= ax2 or ay1 <= ay2:
                print("Ошибка: первый прямоугольник некорректен")
                continue
                
            if bx1 >= bx2 or by1 <= by2:
                print("Ошибка: второй прямоугольник некорректен")
                continue
            
            # Вычисление результатов
            inter = intersection_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
            union = union_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
            
            # Вывод результатов
            print(f"\nРезультаты:")
            print(f"Площадь пересечения: {inter}")
            print(f"Площадь объединения: {union}")
            
        except ValueError:
            print("Ошибка: введите 4 целых числа для каждого прямоугольника")
        except KeyboardInterrupt:
            print("\nВыход из программы")
            break

if __name__ == "__main__":
    ax1, ay1, ax2, ay2 = 0, 2, 4, 1
    bx1, by1, bx2, by2 = 3, 3, 5, 1
    
    main(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
