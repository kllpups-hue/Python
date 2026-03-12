import datetime
import calendar

DIGITS = {
    '0': [" *** ", "*   *", "*   *", "*   *", "*   *", "*   *", " *** "],
    '1': ["  *  ", " **  ", "* *  ", "  *  ", "  *  ", "  *  ", "*****"],
    '2': [" *** ", "*   *", "    *", "   * ", "  *  ", " *   ", "*****"],
    '3': [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "],
    '4': ["   * ", "  ** ", " * * ", "*  * ", "*****", "   * ", "   * "],
    '5': ["*****", "*    ", "**** ", "    *", "    *", "*   *", " *** "],
    '6': [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "],
    '7': ["*****", "    *", "   * ", "  *  ", " *   ", " *   ", " *   "],
    '8': [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "],
    '9': [" *** ", "*   *", "*   *", " ****", "    *", "    *", " *** "],
    ' ': ["     ", "     ", "     ", "     ", "     ", "     ", "     "]
}



def get_weekday(day, month, year):
    """определяем какому дню недели соответствует эта дата"""
    try:
        if month < 3:
            month += 12
            year -= 1
        k = year % 100
        j = year // 100
        # Формула Зеллера
        h = (day + (13 * (month + 1)) // 5 + k + k // 4 + j // 4 - 2 * j) % 7
    
        # В алгоритме Зеллера: 0 = суббота, 1 = воскресенье, ..., 6 = пятница
        days_ru = ["Суббота", "Воскресенье", "Понедельник", "Вторник", 
              "Среда", "Четверг", "Пятница"]
        return days_ru[h]
    except ValueError:
        return "Некорректная дата"

def is_leap_year(year):
    """определяем високосный это был год, или нет"""
    return calendar.isleap(year)

def calculate_age(day, month, year):
    """вычисляем сколько сейчас лет пользователю"""
    today = datetime.date.today()
    birth_date = datetime.date(year, month, day)
    
    age = today.year - birth_date.year
    
    # Проверяем, был ли день рождения в этом году
    # Если сегодня месяц меньше месяца рождения ИЛИ (месяц тот же, но день еще не наступил)
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
        
    return age

def draw_date_stars(date_string):
    # Преобразуем дату в список символов 
    parts = date_string.split() # ['дд', 'мм', 'гггг']
    chars_to_draw = []
    for part in parts:
        for char in part:
            chars_to_draw.append(char)
        chars_to_draw.append(' ') 
    if chars_to_draw and chars_to_draw[-1] == ' ':
        chars_to_draw.pop()
    height = 7
    
    # Печатаем построчно
    for row in range(height):
        line = ""
        for char in chars_to_draw:
            if char in DIGITS:
                line += DIGITS[char][row] + " " 
            else:
                line += DIGITS[' '][row] + " "
        print(line)

def main():
    print()    
    # Запрос данных у пользователя с проверкой ввода
    while True:
        try:
            day = int(input("Введите день рождения (1-31): "))
            month = int(input("Введите месяц рождения (1-12): "))
            year = int(input("Введите год рождения (например, 1990): "))
            
            datetime.date(year, month, day)
            break
        except ValueError:
            print("Ошибка: Введена некорректная дата. Попробуйте снова.")

    print(f"Результат расчета: ")
    # 1. выводим День недели
    weekday = get_weekday(day, month, year)
    print(f"День недели вашего рождения: {weekday}")
    
    # 2. выводим какой был год
    if is_leap_year(year):
        print(f"Год {year} был високосным (в феврале было 29 дней).")
    else:
        print(f"Год {year} был обычным (не високосным).")
        
    # 3. выводим Возраст
    age = calculate_age(day, month, year)
    print(f"Ваш текущий возраст: {age} лет.")
    
    # 4. Вывод дату рождения
    print("\n Ваша дата рождения ")
    formatted_date = f"{day:02d} {month:02d} {year}"
    draw_date_stars(formatted_date)

if __name__ == "__main__":
    main()