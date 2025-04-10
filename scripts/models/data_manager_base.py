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
