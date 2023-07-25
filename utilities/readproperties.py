import os
from utilities import CustomLogger


class ReadConfig:
    @staticmethod
    def get_logs_directory():
        current_directory = os.path.dirname(__file__)
        current_directory = current_directory.replace("utilities", "")
        logs_directory = os.path.join(current_directory, 'Logs')
        return logs_directory
