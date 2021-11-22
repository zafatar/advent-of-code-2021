# src/DayFactory.py

from src.Day import Day
from src.Days.Day1 import Day1

advent_days = {
    'Day1': Day1(),
}


class DayFactory:
    """
    Day Factory class
    """
    @staticmethod
    def instantiate(day_number=0):
        return advent_days["Day" + str(day_number)]
