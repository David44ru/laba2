import random

def find_multiples(numbers, x):
    return list(filter(lambda num: num % x == 0, numbers))

def get_number():
    while True:
        user_input = input("Введите число X, чтобы найти числа, кратные X: ")
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Ошибка: введите корректное число.")

def main():
    while True:
        # Генерация списка случайных чисел
        numbers = [random.randint(0, 200) for _ in range(10)]
        print(f"Сгенерированный список: {numbers}")

        # Получаем число X от пользователя
        x = get_number()

        # Поиск всех чисел, кратных X
        multiples = find_multiples(numbers, x)

        if multiples:
            print(f"Числа, кратные {x}: {multiples}")
        else:
            print(f"Нет чисел, кратных {x}, в списке.")

        # Спрашиваем, хочет ли пользователь продолжить
        while True:
            continue_program = input("Хотите продолжить? (да/нет): ").strip().lower()
            if continue_program in ['да', 'нет']:
                break
            else:
                print("Ошибка: введите 'да' или 'нет'.")
        
        if continue_program == 'нет':
            print("Выход из программы.")
            break

if __name__ == "__main__":
    main()
