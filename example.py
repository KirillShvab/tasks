from area_lib import AnotherShape

if __name__ == '__main__':
    shape_1 = AnotherShape(2)  # круг
    shape_2 = AnotherShape(3, 3, 5)  # треугольник

    print(f'Площадь круга: {shape_1.area():.2f}')
    print(f'Площадь круга: {shape_2.area():.2f}')
