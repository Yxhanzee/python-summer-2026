"""
Консольный трекер привычек.
Позволяет отмечать привычки, сохранять их в файл и смотреть статистику.
"""
import datetime
import os
Habits_file = 'habits.txt'
if not os.path.exists(Habits_file):
    with open(Habits_file,'w',encoding='utf-8') as f:
        pass
def show_menu() -> str:
    print('\n=== Трекер привычек ===')
    print('1. Отметить привычку')
    print('2. Показать статистику')
    print('3. Выйти')
    return input('Выберите действие: ').strip()
def load_habits(filename:str = Habits_file) -> list:
    if not os.path.exists(filename):
        return []
    with open(filename, 'r', encoding = 'utf-8') as f:
        lines = f.readlines()
        records = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if "|" in line:
                date_str, habit = line.split('|',1)
                date_str = date_str.strip()
                habit = habit.strip()
                records.append((date_str,habit))
            else:
                print(f'Ошибка: неверный формат строки : {line}')
    return records
def mark_habit(filename:str = Habits_file) -> None:
    habit = input('Пожалуйста, введите привычку:').strip()
    if not habit:
        print('Название привычки не инициализировано.')
        return
    today = datetime.date.today().isoformat()
    with open(filename,'a',encoding='utf-8') as f:
        f.write(f'{today} | {habit}\n')
    print(f'Привычка "{habit}" отмечена!')
def show_stats(filename:str = Habits_file) -> None:
    records = load_habits(filename)
    if not records:
        print(f'Статистика пока отсутствует. Начните отмечать привычки уже сейчас!')
        return 
    counts = {}
    for date_str, habit in records:
        counts[habit] = counts.get(habit,0) + 1
    total = len(records)
    print(f'\n Общее количество отметок: {total}')
    print('Статистика по привычкам:')
    for habit, count in counts.items():
        print(f'  {habit}: {count} раз(а)')
    most_common = max(counts,key = counts.get)
    least_common = min(counts, key = counts.get)
    print(f'Самая популярная привычка: "{most_common}" ({counts[most_common]} раз)')
    print(f"Самая редкая привычка: '{least_common}' ({counts[least_common]} раз)")
def main() -> None:
    if not os.path.exists(Habits_file):
        with open(Habits_file,'w',encoding='utf-8') as f:
            pass
    while True:
        choice = show_menu()
        if choice == '1':
            mark_habit()
        elif choice == '2':
            show_stats()
        elif choice == '3':
            print('До свидания!')
            break
        else:
            print('Некорректный ввод. Попробуйте снова.')
if __name__ == "__main__":
    main()
