def get_number():
    # Генератор возвращает нечетные числа из диапазона range(30)
    for num in range(30):
        if num % 2 != 0:
            yield num

def process_odd_numbers():
    # Создаем генератор
    gen = get_number()
    
    # Создаем список для хранения нечетных чисел
    odd_numbers = []

    # Используем цикл for, чтобы получить все нечетные числа
    for idx, num in enumerate(gen, start=1):
        odd_numbers.append(num)

    if len(odd_numbers) >= 5:
        print("Первое нечетное число:", odd_numbers[0])
        print("Пятое нечетное число:", odd_numbers[4])
        print("Последнее нечетное число:", odd_numbers[-1])
    else:
        print("Недостаточно нечетных чисел в диапазоне.")

def main():
    while True:
        # Выполняем основную логику
        process_odd_numbers()

        # Бесконечный цикл с запросом на продолжение
        cont = input("Хотите продолжить? (да/нет): ").strip().lower()
        if cont == 'нет':
            print("Завершение программы.")
            break
        elif cont != 'да':
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()

