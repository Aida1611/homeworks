import datetime

parking_data = {}  # Хранилище информации о талонах
PRICE_PER_HOUR = 50  # Стоимость парковки за 1 час


def issue_ticket():
    car_number = input("Введите номер машины: ").strip()

    if not car_number or car_number.isalpha() or car_number.isdigit():
        print("Ошибка: Номер машины должен содержать и буквы, и цифры.")
        return

    ticket_number = len(parking_data) + 123456  # Генерация номера талона
    entry_time = datetime.datetime.now()  # Фиксация времени въезда

    parking_data[ticket_number] = {"car_number": car_number, "entry_time": entry_time}

    print("\nТалон выдан!")
    print(f"Номер талона: {ticket_number}")
    print(f"Номер машины: {car_number}")
    print(f"Время въезда: {entry_time.strftime('%Y-%m-%d %H:%M:%S')}\n")

def return_ticket():
    try:
        ticket_number = int(input("Введите номер талона: ").strip())  # Вводим номер талона
    except ValueError:
        print("Ошибка: номер талона должен быть числом!\n")
        return  # Если введено не число, завершить выполнение функции

    if ticket_number in parking_data:  # Проверяем, существует ли такой талон
        car_info = parking_data.pop(ticket_number)  # Удаляем талон из базы
        exit_time = datetime.datetime.now()
        duration = exit_time - car_info["entry_time"]


        # Рассчитываем часы с округлением вверх
        total_hours = duration.total_seconds() / 3600
        rounded_hours = int(total_hours) + (1 if total_hours % 1 > 0 else 0)

        # Итоговая стоимость
        total_price = rounded_hours * PRICE_PER_HOUR

        print("\nСдача талона:")
        print(f"Номер талона: {ticket_number}")
        print(f"Номер машины: {car_info['car_number']}")
        print(f"Время въезда: {car_info['entry_time'].strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Время выезда: {exit_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Продолжительность парковки: {rounded_hours} час(а/ов)")
        print(f"Стоимость парковки: {total_price} сом\n")
    else:
        print("Ошибка: Неверный номер талона! Такой талон не существует.\n")

def parking():
    while True:
        print("1. Выдача талона")
        print("2. Сдача талона")
        print("3. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            issue_ticket()
        elif choice == "2":
            return_ticket()
        elif choice == "3":
            print("Выход из системы.")
            break
        else:
            print("Неверный ввод, попробуйте снова.")

parking()