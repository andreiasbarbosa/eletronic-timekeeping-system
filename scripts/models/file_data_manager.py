import csv
import os
from models.data_manager_base import DataManagerBase


class FileDataManager(DataManagerBase):
    def __init__(self):
        pass

    def create_csv(self):
        folder = "data"
        filename = "data.csv"
        self.csv_path = os.path.join(folder, filename)
        file_exists = os.path.exists(self.csv_path)

        if not file_exists:
            columns = [
                "Nome", "Data", "Hora inicio", "Hora descanso",
                "Hora retorno descanso", "Hora fim", "Horas trabalhadas"
            ]

            with open(
                self.csv_path,
                "w",
                newline="",
                encoding="utf-8"
            ) as data_csv:
                writer = csv.writer(data_csv, delimiter=",")
                writer.writerow(columns)

    def save_entry(self, entry):
        line = [
                entry.name, entry.date, entry.start_time, entry.lunch_start,
                entry.lunch_end, entry.end_time, entry.hours_worked
            ]

        with open(
                self.csv_path,
                "a",
                newline="",
                encoding="utf-8"
        ) as data_csv:
            writer = csv.writer(data_csv, delimiter=",")
            writer.writerow(line)
