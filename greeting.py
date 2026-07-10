import datetime

def main():
    name = input("Как тебя зовут? ")
    current_hour = datetime.datetime.now().hour
    
    if 6 <= current_hour < 12:
        time_of_day = "Доброе утро"
    elif 12 <= current_hour < 18:
        time_of_day = "Добрый день"
    elif 18 <= current_hour < 23:
        time_of_day = "Добрый вечер"
    else:
        time_of_day = "Доброй ночи"
    
    print(f"{time_of_day}, {name}! Ты уже настроил Git, GitHub и VS Code.")
    print(f"Текущее время: {datetime.datetime.now().strftime('%H:%M')}")

if __name__ == "__main__":
    main()