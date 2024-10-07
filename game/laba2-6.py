import random

def play_game():
    choices = ['камень', 'ножницы', 'бумага']
    
    while True:
        user_choice = input("Выберите: камень, ножницы или бумага? ").strip().lower()
        
        if user_choice not in choices:
            print("Неверный ввод, попробуйте снова.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Компьютер выбрал: {computer_choice}")
        
        if user_choice == computer_choice:
            print("Ничья!")
        elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
             (user_choice == 'ножницы' and computer_choice == 'бумага') or \
             (user_choice == 'бумага' and computer_choice == 'камень'):
            print("Вы выиграли!")
        else:
            print("Компьютер выиграл!")
        
        cont = input("Хотите продолжить? (да/нет): ").strip().lower()
        if cont == 'нет':
            print("Спасибо за игру!")
            break

if __name__ == "__main__":
    play_game()
