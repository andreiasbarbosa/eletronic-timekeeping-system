from models.file_data_manager import FileDataManager
from models.time_keeping_entry import TimeKeepingEntry
from models.utilities import Utilities


if __name__ == '__main__':
    print('Olá Andréia!')
    user_name = "Andréia Barbosa"
    date_today = Utilities.get_day_system()
    file_data_manager = FileDataManager()
    entry = TimeKeepingEntry(date_today, user_name)
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
            entry.start_time = Utilities.get_hour_system()
            print(
                f"Operação registrada com sucesso!"
                f"Você registrou às {entry.start_time}.\n"
            )

        elif user_input == "2":
            entry.lunch_start = Utilities.get_hour_system()
            print(
                f"Operação registrada com sucesso!"
                f"Você registrou às {entry.lunch_start}.\n"
            )

        elif user_input == "3":
            entry.lunch_end = Utilities.get_hour_system()
            print(
                f"Operação registrada com sucesso!"
                f"Você registrou às {entry.lunch_end}.\n"
            )

        else:
            entry.end_time = Utilities.get_hour_system()
            print(
                f"Operação registrada com sucesso!"
                f"Você registrou às {entry.end_time}.\n"
            )
        count_data += 1

    file_data_manager.create_csv()
    file_data_manager.save_entry(entry)
