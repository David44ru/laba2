from datetime import datetime

def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def get_birth_date():
    while True:
        user_input = input("Введите дату рождения в формате день/месяц/год: ")
        try:
            birth_date = datetime.strptime(user_input, "%d/%m/%Y")
            return birth_date
        except ValueError:
            print("Ошибка: неверный формат даты. Попробуйте снова.")

def main():
    while True:
        birth_date = get_birth_date()
        age = calculate_age(birth_date)
        print(f"Ваш возраст: {age} лет(года).")

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
