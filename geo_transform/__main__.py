from geo_transform import *

def menu():
    while True:
        print("Выберите функцию:")
        print("1. Преобразовать декартовые координаты в сферические")
        print("2. Преобразовать сферические координаты в декартовые")
        print("3. Перевести сферические координаты (градусы -> радианы) и преобразовать в декартовые координаты")
        print("4. Перевести сферические координаты: из градусов в радианы")
        print("5. Перевести сферические координаты: из радиан в градусы")
        print("6. Преобразовать декартовые координаты в сферические из файла")
        print("0. Выйти отсюдова")

        try:
            choice = int(input("Введите номер программы: "))
        except ValueError:
            print("Пожалуйста, введите число.")
            continue

        if choice == 0:
            print("Выход из программы.")
            break

        elif choice == 1:
            try:
                a = float(input("Введите координату X: "))
                b = float(input("Введите координату Y: "))
                c = float(input("Введите координату Z: "))
                result_rad = cartesian_to_spherical(a, b, c)
                theta_rad, phi_rad, r_val = result_rad
                theta_deg, phi_deg = rad_to_deg(theta_rad, phi_rad)
                result = f'Сферические координаты в радианах (θ, ϕ, r): ({theta_rad:.4f}, {phi_rad:.4f}, {r_val:.4f})\n'
                result += f'Сферические координаты в градусах (θ, ϕ): ({theta_deg:.4f}, {phi_deg:.4f})'
                print(result)
                write_results_to_file(result)
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == 2:
            try:
                a = float(input("Введите азимутальный угол θ (в радианах): "))
                b = float(input("Введите полярный угол ϕ (в радианах): "))
                c = float(input("Введите радиус r: "))

                result = f'Декартовые координаты(x, y, z): {spherical_to_cartesian(c, a, b)}'
                print(result)
                write_results_to_file(result)
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == 3:
            try:
                a = float(input("Введите азимутальный угол θ (в градусах): "))
                b = float(input("Введите полярный угол ϕ (в градусах): "))
                c = float(input("Введите радиус r: "))
                a, b = deg_to_rad(a, b)
                result = f'Декартовые координаты(x, y, z): {spherical_to_cartesian(c, a, b)}'
                print(result)
                write_results_to_file(result)
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == 4:
            try:
                a = float(input("Введите азимутальный угол θ (в градусах): "))
                b = float(input("Введите полярный угол ϕ (в градусах): "))

                result = f'Сферические координаты азимутальный угол и полярный (в радиан): {deg_to_rad(a, b)}'
                print(result)
                write_results_to_file(result)
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == 5:
            try:
                a = float(input("Введите азимутальный угол θ (в радиан): "))
                b = float(input("Введите полярный угол ϕ (в радиан): "))

                result = f'Сферические координаты азимутальный угол и полярный (в градусах): {rad_to_deg(a, b)}'
                print(result)
                write_results_to_file(result)
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == 6:
            try:
                path = input("Введите путь к файлу: ")
                input_list = read_coordinates_from_file(path)
                if input_list:
                    for coordinates in input_list:
                        if len(coordinates) == 3:
                            x,y,z = coordinates
                            spherical_rad = cartesian_to_spherical(x, y, z)
                            spherical_deg = rad_to_deg(spherical_rad[0], spherical_rad[1])
                            result = f'Для координат ({x}, {y}, {z}):\n'
                            result += f'Сферические координаты в радианах (θ, ϕ, r): {spherical_rad}\n'
                            result += f'Сферические координаты в градусах (θ, ϕ): {spherical_deg}'
                            print(result)
                            write_results_to_file(result)
                        else: 
                            print("Ошибка: а строке должно быть 3 числа")
            except ValueError as e:
                print(f"Ошибка: {e}")

menu()