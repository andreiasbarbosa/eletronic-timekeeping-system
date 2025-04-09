import csv
import os
from datetime import datetime


class DataManagerBase:
    def __init__(self, date, start_time, lunch_start, lunch_end, end_time):
        self.name = "Andréia"
        self.date = date
        self.start_time = start_time
        self.lunch_start = lunch_start
        self.lunch_end = lunch_end
        self.end_time = end_time
        self.hours_worked = 0

    def get_hour_system(self):
        return datetime.now().strftime("%H:%M:%S")


class FileDataManager(DataManagerBase):
    def __init__(self, date):
        super().__init__(date, "", "", "", "")

    def create_csv(self):
        # verifica se o arquivo já existe
        file_exists = os.path.exists("data.csv")

        collums = [
            "Nome", "Data", "Hora inicio", "Hora descanso",
            "Hora retorno descanso", "Hora fim", "Horas trabalhadas"]

        lines = [self.name, self.date, self.start_time,
                 self.lunch_start, self.lunch_end, self.end_time,
                 self.hours_worked]

        with open("data.csv", "a", newline="", encoding="utf-8") as data_csv:
            writer = csv.writer(data_csv, delimiter=",")
            if not file_exists:
                writer.writerow(collums)

            writer.writerow(lines)

    def calculate_hours(self):
        pass


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
