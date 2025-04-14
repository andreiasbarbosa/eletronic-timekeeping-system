from datetime import datetime


class Utilities():
    def __init__(self):
        pass

    @staticmethod
    def calculate_hours(start_time, lunch_start, lunch_end, end_time):
        fmt = "%H:%M"
        start = datetime.strptime(start_time, fmt)
        lunch_start = datetime.strptime(lunch_start, fmt)
        lunch_end = datetime.strptime(lunch_end, fmt)
        end = datetime.strptime(end_time, fmt)

        work_before_lunch = lunch_start - start
        work_after_lunch = end - lunch_end
        total = work_before_lunch + work_after_lunch

        total_seconds = int(total.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60

        return f"{hours:02d}:{minutes:02d}"

    @staticmethod
    def get_hour_system():
        return datetime.now().strftime("%H:%M:%S")

    @staticmethod
    def get_day_system():
        return datetime.now().strftime("%Y-%m-%d")
