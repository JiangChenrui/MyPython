
import datetime
import random
import time


def get_last_tuesday_start():
    today = datetime.datetime(2023, 6, 11)
    weekday = today.weekday()
    if weekday == 1:
        return int(datetime.datetime(today.year, today.month, today.day, 0, 0, 0).timestamp())
    else:
        days_to_last_tuesday = (weekday - 1) % 7
        last_tuesday = today - datetime.timedelta(days=days_to_last_tuesday)
        return int(datetime.datetime(last_tuesday.year, last_tuesday.month, last_tuesday.day, 0, 0, 0).timestamp())


class UserClub(object):

    club_chest_history = []

    def reset_club_chest(self):
        chest_data = [random.randint(1, 6), get_last_tuesday_start()]
        self.club_chest_history.append(chest_data)
        while len(self.club_chest_history) > 4:
            self.club_chest_history.pop(0)

chest_history_list = [
    [1, 1684814400000],
    [2, 1686024000000],
    [3, 1685419200000],
    [4, 1687233600000],
]

next_tuesday = 1687838400

# chest_history_list = [k for k in chest_history_list if k[1] >= (next_tuesday - 86400 * 4 * 7) * 1000]
chest_history_list = list(filter(lambda x: x[1] >= (next_tuesday - 86400 * 4 * 7) * 1000, chest_history_list))


print(chest_history_list)