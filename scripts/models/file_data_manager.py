import csv
import os
from models.data_manager_base import DataManagerBase


class FileDataManager(DataManagerBase):
    def __init__(self, date):
        super().__init__(date, "", "", "", "")

    def create_csv(self):
        folder = "data"
        filename = "data.csv"
        csv_path = os.path.join(folder, filename)
        file_exists = os.path.exists(csv_path)

        columns = [
            "Nome", "Data", "Hora inicio", "Hora descanso",
            "Hora retorno descanso", "Hora fim", "Horas trabalhadas"
        ]

        lines = [self.name, self.date, self.start_time,
                 self.lunch_start, self.lunch_end, self.end_time,
                 self.hours_worked]

        with open(csv_path, "a", newline="", encoding="utf-8") as data_csv:
            writer = csv.writer(data_csv, delimiter=",")
            if not file_exists:
                writer.writerow(columns)

            writer.writerow(lines)

    def calculate_hours(self):
        pass
