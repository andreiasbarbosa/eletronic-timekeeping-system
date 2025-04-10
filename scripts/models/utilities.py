from datetime import datetime


class Utilities():
    def __init__(self):
        pass

    @staticmethod
    def calculate_hours():
        pass

    @staticmethod
    def get_hour_system():
        return datetime.now().strftime("%H:%M:%S")

    @staticmethod
    def get_day_system():
        return datetime.now().strftime("%Y-%m-%d")
