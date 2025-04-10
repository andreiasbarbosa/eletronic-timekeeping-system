from datetime import datetime
from models.file_data_manager import FileDataManager


if __name__ == '__main__':
    print('Olá Andréia!')
    date_today = datetime.now().strftime("%Y-%m-%d")
    new_day = FileDataManager(date_today)
    count_data = 0

    while count_data < 4:
        user_input = input(
            "1 - Iniciar jornada\n"
            "2 - Iniciar descanso\n"
            "3 - Retorno do descanso\n"
            "4 - Finalizar jornada\n"
            "Digite uma das opções:"
        )

        if user_input == "1":
            new_day.start_time = new_day.get_hour_system()
            print(
                f"Operação registrada com sucesso!"
                f"Você registrou às {new_day.start_time}.\n"
            )

        elif user_input == "2":
            new_day.lunch_start = new_day.get_hour_system()
            print(
                f"Operação registrada com sucesso!"
                f"Você registrou às {new_day.lunch_start}.\n"
            )

        elif user_input == "3":
            new_day.lunch_end = new_day.get_hour_system()
            print(
                f"Operação registrada com sucesso!"
                f"Você registrou às {new_day.lunch_end}.\n"
            )

        else:
            new_day.end_time = new_day.get_hour_system()
            print(
                f"Operação registrada com sucesso!"
                f"Você registrou às {new_day.end_time}.\n"
            )
        count_data += 1

    new_day.create_csv()
